# Copyright 2024 Flower Labs GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Test Fleet Simulation Engine API."""
import asyncio
import threading
from itertools import cycle
from math import pi
from time import sleep
from typing import Dict, Optional, Set
from unittest import IsolatedAsyncioTestCase
from uuid import UUID

from flwr.client import Client, NumPyClient
from flwr.client.clientapp import ClientApp
from flwr.common import (
    Config,
    ConfigsRecord,
    GetPropertiesIns,
    Message,
    Metadata,
    Scalar,
)
from flwr.common.constant import MESSAGE_TYPE_GET_PROPERTIES
from flwr.common.recordset_compat import getpropertiesins_to_recordset
from flwr.common.serde import message_from_taskres, message_to_taskins
from flwr.server.superlink.fleet.vce.vce_api import (
    NodeToPartitionMapping,
    _register_nodes,
    start_vce,
)
from flwr.server.superlink.state import InMemoryState, StateFactory


class DummyClient(NumPyClient):
    """A dummy NumPyClient for tests."""

    def get_properties(self, config: Config) -> Dict[str, Scalar]:
        """Return properties by doing a simple calculation."""
        result = float(config["factor"]) * pi

        # store something in context
        self.context.state.configs_records["result"] = ConfigsRecord({"result": result})
        return {"result": result}


def get_dummy_client(cid: str) -> Client:  # pylint: disable=unused-argument
    """Return a DummyClient converted to Client type."""
    return DummyClient().to_client()


client_app = ClientApp(
    client_fn=get_dummy_client,
)


def terminate_simulation(f_stop: asyncio.Event, sleep_duration: int) -> None:
    """Set event to terminate Simulation Engine after `sleep_duration` seconds."""
    sleep(sleep_duration)
    f_stop.set()


def start_and_shutdown(
    existing_state_factory: Optional[StateFactory] = None,
    nodes_mapping: Optional[NodeToPartitionMapping] = None,
    duration: int = 10,
) -> None:
    """Start Simulation Engine and terminate after specified number of seconds."""
    f_stop = asyncio.Event()

    # Initialize StateFactory
    if nodes_mapping:
        if existing_state_factory is None:
            raise ValueError(
                "If you specify a node mapping, you must pass a StateFactory."
            )
        state_factory = existing_state_factory
    else:
        state_factory = StateFactory(":flwr-in-memory-state:")

    # Setup thread that will set the f_stop event, triggering the termination of all
    # asyncio logic in the Simulation Engine. It will also terminate the Backend.
    termination_th = threading.Thread(
        target=terminate_simulation, args=(f_stop, duration)
    )
    termination_th.start()

    start_vce(
        num_supernodes=50,
        client_app_module_name="vce_api_test:client_app",
        backend_name="ray",
        backend_config_json_stream="{}",  # an empty json stream (an empty config)
        state_factory=state_factory,
        working_dir="",
        f_stop=f_stop,
        existing_nodes_mapping=nodes_mapping,
    )

    # Trigger stop event
    f_stop.set()

    termination_th.join()


class AsyncTestFleetSimulationEngineRayBackend(IsolatedAsyncioTestCase):
    """A basic class that enables testing asyncio functionalities."""

    def test_start_and_shutdown(self) -> None:
        """Start Simulation Engine Fleet and terminate it."""
        start_and_shutdown()

    # pylint: disable=too-many-locals
    def test_start_and_shutdown_with_tasks_in_state(self) -> None:
        """Run Simulation Engine with some TasksIns in State.

        This test creates a few nodes and submits a few messages that need to be
        executed by the Backend. In order for that to happen the asyncio
        producer/consumer logic must function.
        """
        num_messages = 113
        num_nodes = 59

        # Register a state and a run_id in it
        run_id = 1234
        state_factory = StateFactory(":flwr-in-memory-state:")
        state: InMemoryState = state_factory.state()  # type: ignore
        state.run_ids.add(run_id)

        # Register a few nodes
        nodes_mapping = _register_nodes(
            num_nodes=num_nodes, state_factory=state_factory
        )

        # Artificially add TaskIns to state so they can be processed
        # by the Simulation Engine logic
        nodes_cycle = cycle(
            nodes_mapping.keys()
        )  # we have more messages than supernodes
        task_ids: Set[UUID] = set()  # so we can retrieve them later
        expected_results = {}
        for i in range(num_messages):
            dst_node_id = next(nodes_cycle)
            # Construct a Message
            mult_factor = 2024 + i
            getproperties_ins = GetPropertiesIns(config={"factor": mult_factor})
            recordset = getpropertiesins_to_recordset(getproperties_ins)
            message = Message(
                content=recordset,
                metadata=Metadata(
                    run_id=run_id,
                    message_id="",
                    group_id="",
                    src_node_id=0,
                    dst_node_id=dst_node_id,  # indicate destination node
                    reply_to_message="",
                    ttl="",
                    message_type=MESSAGE_TYPE_GET_PROPERTIES,
                ),
            )
            # Convert Message to TaskIns
            taskins = message_to_taskins(message)
            # Instert in state
            task_id = state.store_task_ins(taskins)
            if task_id:
                # Add to UUID set
                task_ids.add(task_id)
                # Store expected output for check later on
                expected_results[task_id] = mult_factor * pi

        # Run
        start_and_shutdown(state_factory, nodes_mapping)

        # Get all TaskRes
        task_res_list = state.get_task_res(task_ids=task_ids, limit=len(task_ids))

        # Check results by first converting to Message
        for task_res in task_res_list:

            message = message_from_taskres(task_res)

            # Verify message content is as expected
            content = message.content
            assert (
                content.configs_records["getpropertiesres.properties"]["result"]
                == expected_results[UUID(task_res.task.ancestry[0])]
            )
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
"""Flower command line interface `log` command."""

import typer
from typing_extensions import Annotated
from logging import INFO
import time


def log(
    run_id: Annotated[
        int,
        typer.Option(case_sensitive=False, help="The Flower run ID to query"),
    ],
    follow: Annotated[
        bool,
        typer.Option(case_sensitive=False, help="Use this flag to follow logstream"),
    ] = True,
) -> None:
    """Get logs from Flower run."""
    from logging import DEBUG

    from flwr.common.grpc import GRPC_MAX_MESSAGE_LENGTH, create_channel
    from flwr.common.logger import log
    from flwr.proto.exec_pb2 import StreamLogsRequest
    from flwr.proto.exec_pb2_grpc import ExecStub

    def on_channel_state_change(channel_connectivity: str) -> None:
        """Log channel connectivity."""
        log(DEBUG, channel_connectivity)

    def stream_logs(run_id, channel_configs, duration):

        start_time = time.time()
        channel = create_channel(**channel_configs)
        channel.subscribe(on_channel_state_change)

        stub = ExecStub(channel)
        req = StreamLogsRequest(run_id=run_id)

        for res in stub.StreamLogs(req):
            print(res.log_output)
            if follow and time.time() - start_time < duration:
                continue
            else:
                log(INFO, "Logstream exceeded duration.")
                break

    CHANNEL_CONFIGS = {
        'server_address': "127.0.0.1:9093",
        'insecure': True,
        'root_certificates': None,
        'max_message_length': GRPC_MAX_MESSAGE_LENGTH,
        'interceptors': None,
    }
    STREAM_DURATION = 60

    try:
        while True:
            stream_logs(run_id, CHANNEL_CONFIGS, STREAM_DURATION)
            time.sleep(5)
            log(INFO, "Reconnecting to logstream.")

    except KeyboardInterrupt:
        log(INFO, "Exiting `flwr log`.")

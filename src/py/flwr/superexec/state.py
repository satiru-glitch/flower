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
"""SuperExec state abstraction."""

from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List, Optional


class RunStatus(Enum):
    """RunStatus Enum."""

    RUNNING = auto()
    FINISHED = auto()
    INTERRUPTED = auto()


class SuperexecState(ABC):
    """Abstract SuperexecState."""

    @abstractmethod
    def initialize(self) -> None:
        """Initialize state."""

    @abstractmethod
    def store_log(self, run_id: int, log_output: str, stream: str = "stderr") -> None:
        """Store a log entry for a given run."""

    @abstractmethod
    def get_logs(self, run_id: int) -> List[str]:
        """Retrieve all log entries for a given run."""

    @abstractmethod
    def update_run_tracker(self, run_id: int, status: RunStatus) -> None:
        """Store or update a RunTracker with the given run_id and status."""

    @abstractmethod
    def get_run_tracker_status(self, run_id: int) -> Optional[RunStatus]:
        """Retrieve the status of a RunTracker by run_id."""

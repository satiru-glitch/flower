"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import flwr.proto.fab_pb2
import flwr.proto.message_pb2
import flwr.proto.node_pb2
import flwr.proto.run_pb2
import flwr.proto.task_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetNodesRequest(google.protobuf.message.Message):
    """GetNodes messages"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    def __init__(self,
        *,
        run_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_id",b"run_id"]) -> None: ...
global___GetNodesRequest = GetNodesRequest

class GetNodesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NODES_FIELD_NUMBER: builtins.int
    @property
    def nodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[flwr.proto.node_pb2.Node]: ...
    def __init__(self,
        *,
        nodes: typing.Optional[typing.Iterable[flwr.proto.node_pb2.Node]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["nodes",b"nodes"]) -> None: ...
global___GetNodesResponse = GetNodesResponse

class PushTaskInsRequest(google.protobuf.message.Message):
    """PushTaskIns messages"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TASK_INS_LIST_FIELD_NUMBER: builtins.int
    @property
    def task_ins_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[flwr.proto.task_pb2.TaskIns]: ...
    def __init__(self,
        *,
        task_ins_list: typing.Optional[typing.Iterable[flwr.proto.task_pb2.TaskIns]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_ins_list",b"task_ins_list"]) -> None: ...
global___PushTaskInsRequest = PushTaskInsRequest

class PushTaskInsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TASK_IDS_FIELD_NUMBER: builtins.int
    @property
    def task_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        task_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_ids",b"task_ids"]) -> None: ...
global___PushTaskInsResponse = PushTaskInsResponse

class PullTaskResRequest(google.protobuf.message.Message):
    """PullTaskRes messages"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NODE_FIELD_NUMBER: builtins.int
    TASK_IDS_FIELD_NUMBER: builtins.int
    @property
    def node(self) -> flwr.proto.node_pb2.Node: ...
    @property
    def task_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        node: typing.Optional[flwr.proto.node_pb2.Node] = ...,
        task_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["node",b"node"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["node",b"node","task_ids",b"task_ids"]) -> None: ...
global___PullTaskResRequest = PullTaskResRequest

class PullTaskResResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TASK_RES_LIST_FIELD_NUMBER: builtins.int
    @property
    def task_res_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[flwr.proto.task_pb2.TaskRes]: ...
    def __init__(self,
        *,
        task_res_list: typing.Optional[typing.Iterable[flwr.proto.task_pb2.TaskRes]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_res_list",b"task_res_list"]) -> None: ...
global___PullTaskResResponse = PullTaskResResponse

class PullServerAppInputsRequest(google.protobuf.message.Message):
    """PullServerAppInputs messages"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    def __init__(self,
        *,
        run_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_id",b"run_id"]) -> None: ...
global___PullServerAppInputsRequest = PullServerAppInputsRequest

class PullServerAppInputsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTEXT_FIELD_NUMBER: builtins.int
    RUN_FIELD_NUMBER: builtins.int
    FAB_FIELD_NUMBER: builtins.int
    @property
    def context(self) -> flwr.proto.message_pb2.Context: ...
    @property
    def run(self) -> flwr.proto.run_pb2.Run: ...
    @property
    def fab(self) -> flwr.proto.fab_pb2.Fab: ...
    def __init__(self,
        *,
        context: typing.Optional[flwr.proto.message_pb2.Context] = ...,
        run: typing.Optional[flwr.proto.run_pb2.Run] = ...,
        fab: typing.Optional[flwr.proto.fab_pb2.Fab] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["context",b"context","fab",b"fab","run",b"run"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["context",b"context","fab",b"fab","run",b"run"]) -> None: ...
global___PullServerAppInputsResponse = PullServerAppInputsResponse

class PushServerAppOutputsRequest(google.protobuf.message.Message):
    """PushServerAppOutputs messages"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    @property
    def context(self) -> flwr.proto.message_pb2.Context: ...
    def __init__(self,
        *,
        run_id: builtins.int = ...,
        context: typing.Optional[flwr.proto.message_pb2.Context] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["context",b"context"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["context",b"context","run_id",b"run_id"]) -> None: ...
global___PushServerAppOutputsRequest = PushServerAppOutputsRequest

class PushServerAppOutputsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___PushServerAppOutputsResponse = PushServerAppOutputsResponse

class PushLogsRequest(google.protobuf.message.Message):
    """PushLogs messages"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    NODE_FIELD_NUMBER: builtins.int
    LOGS_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    @property
    def node(self) -> flwr.proto.node_pb2.Node: ...
    @property
    def logs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        run_id: builtins.int = ...,
        node: typing.Optional[flwr.proto.node_pb2.Node] = ...,
        logs: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["node",b"node"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["logs",b"logs","node",b"node","run_id",b"run_id"]) -> None: ...
global___PushLogsRequest = PushLogsRequest

class PushLogsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STATUS_FIELD_NUMBER: builtins.int
    status: typing.Text
    def __init__(self,
        *,
        status: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["status",b"status"]) -> None: ...
global___PushLogsResponse = PushLogsResponse

"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import flwr.proto.clientappio_pb2
import grpc

class ClientAppIoStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    GetToken: grpc.UnaryUnaryMultiCallable[
        flwr.proto.clientappio_pb2.GetTokenRequest,
        flwr.proto.clientappio_pb2.GetTokenResponse]
    """Get token"""

    PullClientAppInputs: grpc.UnaryUnaryMultiCallable[
        flwr.proto.clientappio_pb2.PullClientAppInputsRequest,
        flwr.proto.clientappio_pb2.PullClientAppInputsResponse]
    """Get Message, Context, and Fab"""

    PushClientAppOutputs: grpc.UnaryUnaryMultiCallable[
        flwr.proto.clientappio_pb2.PushClientAppOutputsRequest,
        flwr.proto.clientappio_pb2.PushClientAppOutputsResponse]
    """Send updated Message and Context"""


class ClientAppIoServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetToken(self,
        request: flwr.proto.clientappio_pb2.GetTokenRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.clientappio_pb2.GetTokenResponse:
        """Get token"""
        pass

    @abc.abstractmethod
    def PullClientAppInputs(self,
        request: flwr.proto.clientappio_pb2.PullClientAppInputsRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.clientappio_pb2.PullClientAppInputsResponse:
        """Get Message, Context, and Fab"""
        pass

    @abc.abstractmethod
    def PushClientAppOutputs(self,
        request: flwr.proto.clientappio_pb2.PushClientAppOutputsRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.clientappio_pb2.PushClientAppOutputsResponse:
        """Send updated Message and Context"""
        pass


def add_ClientAppIoServicer_to_server(servicer: ClientAppIoServicer, server: grpc.Server) -> None: ...

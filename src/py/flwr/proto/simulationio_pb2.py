# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/simulationio.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import log_pb2 as flwr_dot_proto_dot_log__pb2
from flwr.proto import message_pb2 as flwr_dot_proto_dot_message__pb2
from flwr.proto import run_pb2 as flwr_dot_proto_dot_run__pb2
from flwr.proto import fab_pb2 as flwr_dot_proto_dot_fab__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x66lwr/proto/simulationio.proto\x12\nflwr.proto\x1a\x14\x66lwr/proto/log.proto\x1a\x18\x66lwr/proto/message.proto\x1a\x14\x66lwr/proto/run.proto\x1a\x14\x66lwr/proto/fab.proto\"\x1d\n\x1bPullSimulationInputsRequest\"\x80\x01\n\x1cPullSimulationInputsResponse\x12$\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x13.flwr.proto.Context\x12\x1c\n\x03run\x18\x02 \x01(\x0b\x32\x0f.flwr.proto.Run\x12\x1c\n\x03\x66\x61\x62\x18\x03 \x01(\x0b\x32\x0f.flwr.proto.Fab\"T\n\x1cPushSimulationOutputsRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\x12$\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x13.flwr.proto.Context\"\x1f\n\x1dPushSimulationOutputsResponse2\xff\x03\n\x0cSimulationIo\x12k\n\x14PullSimulationInputs\x12\'.flwr.proto.PullSimulationInputsRequest\x1a(.flwr.proto.PullSimulationInputsResponse\"\x00\x12n\n\x15PushSimulationOutputs\x12(.flwr.proto.PushSimulationOutputsRequest\x1a).flwr.proto.PushSimulationOutputsResponse\"\x00\x12\\\n\x0fUpdateRunStatus\x12\".flwr.proto.UpdateRunStatusRequest\x1a#.flwr.proto.UpdateRunStatusResponse\"\x00\x12G\n\x08PushLogs\x12\x1b.flwr.proto.PushLogsRequest\x1a\x1c.flwr.proto.PushLogsResponse\"\x00\x12k\n\x14GetFederationOptions\x12\'.flwr.proto.GetFederationOptionsRequest\x1a(.flwr.proto.GetFederationOptionsResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.simulationio_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PULLSIMULATIONINPUTSREQUEST']._serialized_start=137
  _globals['_PULLSIMULATIONINPUTSREQUEST']._serialized_end=166
  _globals['_PULLSIMULATIONINPUTSRESPONSE']._serialized_start=169
  _globals['_PULLSIMULATIONINPUTSRESPONSE']._serialized_end=297
  _globals['_PUSHSIMULATIONOUTPUTSREQUEST']._serialized_start=299
  _globals['_PUSHSIMULATIONOUTPUTSREQUEST']._serialized_end=383
  _globals['_PUSHSIMULATIONOUTPUTSRESPONSE']._serialized_start=385
  _globals['_PUSHSIMULATIONOUTPUTSRESPONSE']._serialized_end=416
  _globals['_SIMULATIONIO']._serialized_start=419
  _globals['_SIMULATIONIO']._serialized_end=930
# @@protoc_insertion_point(module_scope)
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from helloworld import service_pb2 as helloworld_dot_service__pb2


class HelloWorldStub(object):
  """HelloWorld service to demo gRPC with
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/HelloWorld/SayHello',
        request_serializer=helloworld_dot_service__pb2.SayHelloRequest.SerializeToString,
        response_deserializer=helloworld_dot_service__pb2.SayHelloResponse.FromString,
        )
    self.GetNumbers = channel.unary_stream(
        '/HelloWorld/GetNumbers',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=helloworld_dot_service__pb2.GetNumbersResponse.FromString,
        )
    self.MultiplyNumbers = channel.stream_stream(
        '/HelloWorld/MultiplyNumbers',
        request_serializer=helloworld_dot_service__pb2.MultiplyNumbersRequest.SerializeToString,
        response_deserializer=helloworld_dot_service__pb2.MultiplyNumbersResponse.FromString,
        )


class HelloWorldServicer(object):
  """HelloWorld service to demo gRPC with
  """

  def SayHello(self, request, context):
    """Say hello to my little friend!
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNumbers(self, request, context):
    """Try a response stream
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MultiplyNumbers(self, request_iterator, context):
    """Try a bidirectional stream
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HelloWorldServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=helloworld_dot_service__pb2.SayHelloRequest.FromString,
          response_serializer=helloworld_dot_service__pb2.SayHelloResponse.SerializeToString,
      ),
      'GetNumbers': grpc.unary_stream_rpc_method_handler(
          servicer.GetNumbers,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=helloworld_dot_service__pb2.GetNumbersResponse.SerializeToString,
      ),
      'MultiplyNumbers': grpc.stream_stream_rpc_method_handler(
          servicer.MultiplyNumbers,
          request_deserializer=helloworld_dot_service__pb2.MultiplyNumbersRequest.FromString,
          response_serializer=helloworld_dot_service__pb2.MultiplyNumbersResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'HelloWorld', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
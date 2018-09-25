from concurrent import futures
from typing import Iterable

import grpc
import logging

import time

from google.protobuf.empty_pb2 import Empty

from helloworld import service_pb2_grpc
from helloworld.service_pb2 import SayHelloResponse, SayHelloRequest, \
    GetNumbersResponse, MultiplyNumbersRequest, MultiplyNumbersResponse
from helloworld.service_pb2_grpc import HelloWorldServicer


class HelloWorldServicer(HelloWorldServicer):

    def __init__(self):
        pass

    # Simple request - response
    def SayHello(self, request: SayHelloRequest, context: grpc.ServicerContext) -> SayHelloResponse:
        return SayHelloResponse(
            text=f'Hi there {request.name}!'
        )

    # Response stream
    def GetNumbers(self, request: Empty, context: grpc.ServicerContext) -> GetNumbersResponse:
        numbers = range(1, 10)
        for number in numbers:
            yield GetNumbersResponse(
                number=number
            )

    # Bi-directional stream
    def MultiplyNumbers(self, request_iterator: Iterable[MultiplyNumbersRequest], context: grpc.ServicerContext) -> Iterable[MultiplyNumbersResponse]:
        for item in request_iterator:
            yield MultiplyNumbersResponse(
                number=item.number * 2
            )


def serve() -> None:
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=5)
    )

    service_pb2_grpc.add_HelloWorldServicer_to_server(HelloWorldServicer(), server)
    server.add_insecure_port('[::]:5000')
    server.start()

    logging.info('gRPC server started!')

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)

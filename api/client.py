import grpc
from google.protobuf.empty_pb2 import Empty

from helloworld.service_pb2 import SayHelloRequest, MultiplyNumbersRequest
from helloworld.service_pb2_grpc import HelloWorldStub


def run():
    channel = grpc.insecure_channel('localhost:5000')
    stub = HelloWorldStub(channel)

    # Sync
    response = stub.SayHello(
        SayHelloRequest(
            name='Johnny'
        )
    )
    print(response)

    # Async
    future = stub.SayHello.future(
        SayHelloRequest(
            name='Johnny'
        )
    )
    response = future.result()
    print(response)

    # Response stream
    for item in stub.GetNumbers(Empty()):
        print(item.number)

    # Bi-directional stream
    number_iterator = (MultiplyNumbersRequest(number=i) for i in range(10))
    for multiplied_item in stub.MultiplyNumbers(number_iterator):
        print(multiplied_item.number)


if __name__ == '__main__':
    run()

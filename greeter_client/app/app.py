import logging
import grpc
import time

from grpc_compiled import greeter_pb2_grpc, greeter_pb2

def run():
    host = "greeter_server"
    port = "50051"
    with grpc.insecure_channel(f"{host}:{port}") as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)
        print(f"Sending request to {host}:{port}...")
        response = stub.SayHello(greeter_pb2.HelloRequest(name="Bob Ross"))
    print(f"Received: {response.message}")


if __name__ == "__main__":
    # wait for server to start
    time.sleep(5)
    logging.basicConfig()
    run()
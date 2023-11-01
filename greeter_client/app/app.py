import logging
import grpc
import time

import os
print(os.listdir())
print(os.listdir("grpc_compiled"))

from grpc_compiled import greeter_pb2, greeter_pb2_grpc

def run():
    host = "greeter_server"
    port = "50051"
    print("Will try to greet world ...")
    with grpc.insecure_channel(f"{host}:{port}") as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(greeter_pb2.HelloRequest(name="Bob Ross"))
    print(f"Received: {response.message}")


if __name__ == "__main__":
    # wait for server to start
    time.sleep(5)
    logging.basicConfig()
    run()
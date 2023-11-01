# gRPC with Python and Docker

## Compiling Protobufs

To be able to compile protobuf files ending with `.proto` you will need the toolkit:

```
pip3 install grpcio-tools
```

To the compile the file `greeter.proto` go into the `grpc_protos` file and execute the following command to compile it:

```
cd grpc_protos
python3 -m grpc_tools.protoc -I. --python_out=../grpc_compiled --grpc_python_out=../grpc_compiled ./greeter.proto
```

This will create `greeter_pb2_grpc.py` and `greeter_pb2.py`. In `greeter_pb2_grpc.py` you will have to adapt the import from this:

```
import greeter_pb2 as greeter__pb2
```

to this:

```
from grpc_compiled import greeter_pb2 as greeter__pb2
```

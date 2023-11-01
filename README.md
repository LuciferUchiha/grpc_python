pip3 install grpcio-tools==1.59.2

python3 -m grpc_tools.protoc -I. --python_out=./grpc_compiled --grpc_python_out=./grpc_compiled ./grpc_protos/

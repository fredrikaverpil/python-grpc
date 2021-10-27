#/bin/bash

# Generate protobuf code from the protos/*.proto file(s)
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./protos/*.proto
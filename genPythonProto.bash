#!/bin/bash
python \
-m grpc_tools.protoc \
-I=./proto \
--python_out=./grpc_server/proto \
--grpc_python_out=./grpc_server/proto ./proto/todo.proto
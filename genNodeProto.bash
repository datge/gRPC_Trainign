#!/bin/bash
protoc-gen-grpc \
--js_out=import_style=commonjs,binary:./grpc_client_node/proto \
--grpc_out=grpc_js:./grpc_client_node/proto \
--proto_path ./proto ./proto/todo.proto
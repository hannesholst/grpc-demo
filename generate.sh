#!/usr/bin/env bash

python -m grpc_tools.protoc \
--include_imports \
--include_source_info \
-Iproto/demo \
-I/usr/local/include \
-Iproto/grpc-gateway/third_party/googleapis \
-Iproto/protobuf/src \
--python_out=. \
--grpc_python_out=. \
--mypy_out=. \
--descriptor_set_out=endpoints/service_descriptor.pb \
helloworld/service.proto
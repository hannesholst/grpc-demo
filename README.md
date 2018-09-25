# gRPC DEMO

## Initial setup

```bash
conda create -n grpc-demo python=3
source activate grpc-demo
```

```bash
pip install grpcio grpcio-tools mypy-protobuf
```

Setup PyCharm Project Interpreter on this environment:
/usr/local/miniconda3/envs/grpc-demo/bin/python

```bash
mkdir proto
cd proto
git submodule add https://github.com/protocolbuffers/protobuf.git
git submodule add https://github.com/grpc-ecosystem/grpc-gateway.git
```

Add them to PyCharm:
/Users/hannesholst/grpc-demo/proto/grpc-gateway/third_party/googleapis
/Users/hannesholst/grpc-demo/proto/protobuf/src

```bash
touch generate.sh
chmod +x generate.sh
```

git submodule update --init --recursive

[Good Tutorial](https://alexandreesl.com/2017/05/02/grpc-transporting-massive-data-with-googles-serialization/)
[gRPC Tutorial](https://grpc.io/docs/tutorials/basic/python.html#client)
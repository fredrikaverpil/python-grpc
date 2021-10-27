# python-grpc

Ping-pong server/client using gRPC.

More over at grpc.io: https://grpc.io/docs/languages/python/quickstart/

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python server.py  # start server
python client.py # start client
# or `python multiprocess.py` to start multiple clients.
```

## Protobuf

The Python proto buffer code was generated via the `generate_protobuf_code.sh` script, using the `pingpong.proto` file.

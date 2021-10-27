import os
from protos import pingpong_pb2, pingpong_pb2_grpc
import time
import grpc


def run():
    counter = 0  # to be sent to server, which it will increment and send back
    pid = os.getpid()
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = pingpong_pb2_grpc.PingPongServiceStub(channel)
        while True:
            try:
                start = time.time()
                response = stub.ping(pingpong_pb2.Ping(count=counter))
                counter = response.count
                if counter % 1000 == 0:
                    # For each 1000...
                    print(f"{time.time()-start} : resp={response.count} : procid={pid}")
            except KeyboardInterrupt:
                print("Keyboard interrupted")
                channel.unsubscribe(close)
                exit()


def close(channel):
    channel.close()


if __name__ == "__main__":
    run()

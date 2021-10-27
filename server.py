from concurrent import futures  # run a threadpool executor
import grpc
from protos import pingpong_pb2, pingpong_pb2_grpc
import time
import threading


class Listener(pingpong_pb2_grpc.PingPongServiceServicer):
    def __init__(self, *args, **kwargs):
        self.counter = 0
        self.last_print_time = time.time()

    def ping(self, request, context):
        self.counter += 1
        if self.counter > 10000:
            delta = time.time() - self.last_print_time
            print(f"10000 calls in {delta} seconds")
            self.last_print_time = time.time()
            self.counter = 0
        return pingpong_pb2.Pong(count=request.count + 1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    pingpong_pb2_grpc.add_PingPongServiceServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")  # ipv6
    server.start()
    # server.wait_for_termination()

    try:
        while True:
            print(f"server on: threads {threading.active_count()}")
            time.sleep(10)
    except KeyboardInterrupt:
        print("Keyboard interrupted")
        server.stop(0)


if __name__ == "__main__":
    serve()

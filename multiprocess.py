from multiprocessing import Process
import client

if __name__ == "__main__":
    count = 2
    processes = {}
    for c in range(count):
        processes[c] = Process(target=client.run)
    for x in range(count):
        processes[x].start()

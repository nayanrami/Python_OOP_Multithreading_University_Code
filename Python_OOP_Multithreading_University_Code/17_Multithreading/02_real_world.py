"""Producer-consumer with queue.Queue.

Queue handles the necessary synchronization internally.
"""

from queue import Queue
import threading
import time

SENTINEL = object()

def producer(queue: Queue):
    for value in range(1, 6):
        queue.put(value)
        print("Produced", value)
    queue.put(SENTINEL)

def consumer(queue: Queue):
    while True:
        item = queue.get()
        try:
            if item is SENTINEL:
                return
            time.sleep(0.01)
            print("Consumed", item, "square =", item * item)
        finally:
            queue.task_done()

def main():
    q = Queue()
    p = threading.Thread(target=producer, args=(q,))
    c = threading.Thread(target=consumer, args=(q,))
    p.start()
    c.start()
    p.join()
    q.join()
    c.join()
    print("Pipeline completed")


if __name__ == "__main__":
    main()

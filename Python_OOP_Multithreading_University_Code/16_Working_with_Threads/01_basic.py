"""Create, start and join threads."""

import threading
import time

def worker(name: str, count: int):
    for i in range(1, count + 1):
        print(f"[{threading.current_thread().name}] {name}: step {i}")
        time.sleep(0.02)

def main():
    t1 = threading.Thread(target=worker, args=("Task-A", 3), name="Worker-A")
    t2 = threading.Thread(target=worker, args=("Task-B", 3), name="Worker-B")

    t1.start()
    t2.start()

    # join() blocks the main thread until each worker has finished.
    t1.join()
    t2.join()
    print("Main: both threads completed")


if __name__ == "__main__":
    main()

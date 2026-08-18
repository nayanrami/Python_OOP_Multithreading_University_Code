"""Semaphore limits how many threads may use a resource concurrently."""

import threading
import time

class ConnectionPool:
    def __init__(self, max_connections: int):
        self._semaphore = threading.Semaphore(max_connections)
        self._inside = 0
        self._guard = threading.Lock()
        self.max_seen = 0

    def use(self, worker_id: int):
        with self._semaphore:
            with self._guard:
                self._inside += 1
                self.max_seen = max(self.max_seen, self._inside)
                current = self._inside
            print(f"Worker {worker_id} entered; active={current}")
            time.sleep(0.02)
            with self._guard:
                self._inside -= 1


def main():
    pool = ConnectionPool(max_connections=2)
    threads = [threading.Thread(target=pool.use, args=(i,)) for i in range(1, 7)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Maximum simultaneous users:", pool.max_seen)


if __name__ == "__main__":
    main()

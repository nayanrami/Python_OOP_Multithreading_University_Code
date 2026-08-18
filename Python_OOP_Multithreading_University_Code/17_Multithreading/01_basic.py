"""Shared counter protected by a Lock."""

import threading

class Counter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment_many(self, times: int):
        for _ in range(times):
            with self._lock:
                self.value += 1

def main():
    counter = Counter()
    threads = [threading.Thread(target=counter.increment_many, args=(10_000,)) for _ in range(4)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Expected:", 40_000)
    print("Actual:  ", counter.value)


if __name__ == "__main__":
    main()

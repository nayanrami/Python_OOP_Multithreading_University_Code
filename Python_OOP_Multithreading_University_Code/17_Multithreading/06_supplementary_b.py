"""Supplement: RLock allows the same thread to acquire repeatedly."""

import threading

lock = threading.RLock()

def nested():
    with lock:
        with lock:
            return "nested lock acquired"

if __name__ == "__main__":
    print(nested())

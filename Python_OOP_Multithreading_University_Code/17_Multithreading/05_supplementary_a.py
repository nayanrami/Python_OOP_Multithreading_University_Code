"""Supplement: Event broadcasts a simple state change."""

import threading

ready = threading.Event()

def worker():
    ready.wait()
    print("worker received event")

if __name__ == "__main__":
    t = threading.Thread(target=worker)
    t.start()
    ready.set()
    t.join()

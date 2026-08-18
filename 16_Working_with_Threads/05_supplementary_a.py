"""Supplement: passing keyword arguments to a thread."""

import threading

def greet(name, times=1):
    for _ in range(times):
        print("Hello", name)

if __name__ == "__main__":
    t = threading.Thread(target=greet, kwargs={"name": "Student", "times": 2})
    t.start()
    t.join()

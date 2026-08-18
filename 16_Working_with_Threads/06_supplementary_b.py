"""Supplement: daemon flag inspection."""

import threading

def task():
    print("daemon worker executed")

if __name__ == "__main__":
    t = threading.Thread(target=task, daemon=True)
    print("daemon:", t.daemon)
    t.start()
    t.join()

"""LeetCode 1116-inspired: Print Zero Even Odd."""

import threading

class ZeroEvenOdd:
    def __init__(self, n: int):
        self.n = n
        self.zero_sem = threading.Semaphore(1)
        self.odd_sem = threading.Semaphore(0)
        self.even_sem = threading.Semaphore(0)

    def zero(self, printNumber) -> None:
        for value in range(1, self.n + 1):
            self.zero_sem.acquire()
            printNumber(0)
            (self.odd_sem if value % 2 else self.even_sem).release()

    def odd(self, printNumber) -> None:
        for value in range(1, self.n + 1, 2):
            self.odd_sem.acquire()
            printNumber(value)
            self.zero_sem.release()

    def even(self, printNumber) -> None:
        for value in range(2, self.n + 1, 2):
            self.even_sem.acquire()
            printNumber(value)
            self.zero_sem.release()


def main():
    obj = ZeroEvenOdd(5)
    out = []
    threads = [
        threading.Thread(target=obj.even, args=(out.append,)),
        threading.Thread(target=obj.odd, args=(out.append,)),
        threading.Thread(target=obj.zero, args=(out.append,)),
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(out)


if __name__ == "__main__":
    main()

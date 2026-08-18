"""LeetCode 1115-inspired: Print FooBar Alternately."""

import threading

class FooBar:
    def __init__(self, n: int):
        self.n = n
        self.foo_turn = threading.Semaphore(1)
        self.bar_turn = threading.Semaphore(0)

    def foo(self, printFoo) -> None:
        for _ in range(self.n):
            self.foo_turn.acquire()
            printFoo()
            self.bar_turn.release()

    def bar(self, printBar) -> None:
        for _ in range(self.n):
            self.bar_turn.acquire()
            printBar()
            self.foo_turn.release()


def main():
    fb = FooBar(4)
    output = []
    t1 = threading.Thread(target=fb.bar, args=(lambda: output.append("bar"),))
    t2 = threading.Thread(target=fb.foo, args=(lambda: output.append("foo"),))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(" ".join(output))


if __name__ == "__main__":
    main()

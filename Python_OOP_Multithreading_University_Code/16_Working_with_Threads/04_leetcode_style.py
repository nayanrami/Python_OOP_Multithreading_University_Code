"""LeetCode 1114-inspired: Print in Order.

Events create a happens-before relationship between first, second and third.
"""

import threading

class Foo:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst) -> None:
        printFirst()
        self.first_done.set()

    def second(self, printSecond) -> None:
        self.first_done.wait()
        printSecond()
        self.second_done.set()

    def third(self, printThird) -> None:
        self.second_done.wait()
        printThird()


def main():
    foo = Foo()
    output = []
    jobs = [
        threading.Thread(target=foo.third, args=(lambda: output.append("third"),)),
        threading.Thread(target=foo.second, args=(lambda: output.append("second"),)),
        threading.Thread(target=foo.first, args=(lambda: output.append("first"),)),
    ]
    for job in jobs:
        job.start()
    for job in jobs:
        job.join()
    print(" ".join(output))


if __name__ == "__main__":
    main()

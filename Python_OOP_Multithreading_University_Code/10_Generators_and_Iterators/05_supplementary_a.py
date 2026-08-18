"""Supplement: Fibonacci generator."""

def fibonacci(count):
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    print(list(fibonacci(10)))

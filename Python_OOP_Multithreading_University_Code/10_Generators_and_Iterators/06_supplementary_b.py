"""Supplement: generator expression."""

if __name__ == "__main__":
    squares = (n * n for n in range(1, 8))
    print(next(squares))
    print(next(squares))
    print(list(squares))

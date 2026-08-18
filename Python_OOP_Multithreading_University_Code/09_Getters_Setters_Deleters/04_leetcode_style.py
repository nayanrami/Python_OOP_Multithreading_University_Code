"""LeetCode 901-inspired: Online Stock Span, with properties for safe inspection."""

class StockSpanner:
    def __init__(self):
        self._stack = []  # pairs: (price, accumulated span)
        self._calls = 0

    @property
    def calls(self) -> int:
        return self._calls

    @property
    def pending_levels(self) -> int:
        return len(self._stack)

    def next(self, price: int) -> int:
        self._calls += 1
        span = 1
        while self._stack and self._stack[-1][0] <= price:
            _, previous_span = self._stack.pop()
            span += previous_span
        self._stack.append((price, span))
        return span


def main():
    spanner = StockSpanner()
    print([spanner.next(p) for p in [100, 80, 60, 70, 60, 75, 85]])
    print("Calls:", spanner.calls)
    print("Internal stack levels:", spanner.pending_levels)


if __name__ == "__main__":
    main()

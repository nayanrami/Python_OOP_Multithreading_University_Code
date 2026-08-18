"""LeetCode 56-inspired interval helper with operator overloading.

Intervals can be ordered using < and checked for overlap using @.
"""

class Interval:
    def __init__(self, start: int, end: int):
        if start > end:
            raise ValueError("start cannot exceed end")
        self.start, self.end = start, end

    def __lt__(self, other):
        return self.start < other.start

    def __matmul__(self, other):
        """Educational operator: a @ b means 'a overlaps b'."""
        return max(self.start, other.start) <= min(self.end, other.end)

    def __repr__(self):
        return f"[{self.start}, {self.end}]"

def merge(intervals):
    intervals = sorted(intervals)
    merged = []
    for current in intervals:
        if not merged or not (merged[-1] @ current):
            merged.append(Interval(current.start, current.end))
        else:
            merged[-1].end = max(merged[-1].end, current.end)
    return merged


def main():
    intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(9, 12)]
    print(merge(intervals))


if __name__ == "__main__":
    main()

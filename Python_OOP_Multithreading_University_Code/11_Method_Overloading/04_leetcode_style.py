"""LeetCode 981-inspired: Time Based Key-Value Store.

An educational convenience method demonstrates optional-argument API design.
"""

from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self._data = {}

    def set(self, key: str, value: str, timestamp: int, metadata: dict | None = None) -> None:
        self._data.setdefault(key, []).append((timestamp, value, metadata or {}))

    def get(self, key: str, timestamp: int) -> str:
        entries = self._data.get(key, [])
        times = [entry[0] for entry in entries]
        index = bisect_right(times, timestamp) - 1
        return "" if index < 0 else entries[index][1]


def main():
    store = TimeMap()
    store.set("course", "Python", 1)
    store.set("course", "Advanced Python", 5, {"semester": 5})
    print(store.get("course", 3))
    print(store.get("course", 5))


if __name__ == "__main__":
    main()

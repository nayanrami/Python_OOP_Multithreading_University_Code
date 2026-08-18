"""LeetCode 706-inspired: Design HashMap.

The client sees put/get/remove; bucket details remain abstracted away.
"""

class MyHashMap:
    def __init__(self, bucket_count: int = 101):
        self._bucket_count = bucket_count
        self._buckets = [[] for _ in range(bucket_count)]

    def _index(self, key: int) -> int:
        return key % self._bucket_count

    def put(self, key: int, value: int) -> None:
        bucket = self._buckets[self._index(key)]
        for i, (old_key, _) in enumerate(bucket):
            if old_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        for old_key, value in self._buckets[self._index(key)]:
            if old_key == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        bucket = self._buckets[self._index(key)]
        self._buckets[self._index(key)] = [(k, v) for k, v in bucket if k != key]


def main():
    table = MyHashMap()
    table.put(1, 10)
    table.put(102, 20)  # same bucket when bucket_count = 101
    print(table.get(1), table.get(102), table.get(2))
    table.remove(1)
    print(table.get(1))


if __name__ == "__main__":
    main()

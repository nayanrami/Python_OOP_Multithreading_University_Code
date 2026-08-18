"""__new__ allocates; __init__ initializes."""

class TrackedObject:
    allocations = 0

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.allocations += 1
        return instance

    def __init__(self, label: str):
        self.label = label

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["label"])


def main():
    a = TrackedObject("A")
    b = TrackedObject.from_dict({"label": "B"})
    print(a.label, b.label)
    print("Allocations:", TrackedObject.allocations)


if __name__ == "__main__":
    main()

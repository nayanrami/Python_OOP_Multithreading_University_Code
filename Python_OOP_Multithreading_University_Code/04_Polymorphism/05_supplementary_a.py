"""Supplement: len() is polymorphic."""

if __name__ == "__main__":
    objects = ["Python", [10, 20, 30], {"a": 1, "b": 2}]
    for obj in objects:
        print(type(obj).__name__, len(obj))

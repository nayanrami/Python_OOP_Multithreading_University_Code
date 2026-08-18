"""Structural interface using typing.Protocol."""

from typing import Protocol, runtime_checkable

@runtime_checkable
class Serializable(Protocol):
    def serialize(self) -> str:
        ...

class Student:
    def __init__(self, name):
        self.name = name

    def serialize(self):
        return f'{{"name": "{self.name}"}}'

class Course:
    def __init__(self, code):
        self.code = code

    def serialize(self):
        return f'{{"code": "{self.code}"}}'

def store(obj: Serializable):
    print("Stored:", obj.serialize())


def main():
    for obj in [Student("Mahi"), Course("PY101")]:
        print("Serializable?", isinstance(obj, Serializable))
        store(obj)


if __name__ == "__main__":
    main()

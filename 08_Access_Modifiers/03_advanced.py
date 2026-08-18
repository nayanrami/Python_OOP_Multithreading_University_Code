"""Name mangling avoids accidental attribute clashes in subclasses."""

class Base:
    def __init__(self):
        self.__state = "base-state"

    def base_state(self):
        return self.__state

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__state = "child-state"

    def child_state(self):
        return self.__state


def main():
    obj = Child()
    print(obj.base_state())
    print(obj.child_state())
    print([name for name in dir(obj) if "state" in name])


if __name__ == "__main__":
    main()

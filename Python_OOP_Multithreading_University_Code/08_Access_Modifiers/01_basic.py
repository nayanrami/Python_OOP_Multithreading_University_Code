"""Public, protected-by-convention and private/name-mangled members."""

class Demo:
    def __init__(self):
        self.public_value = "public"
        self._internal_value = "protected by convention"
        self.__private_value = "name-mangled"

    def reveal_private(self):
        return self.__private_value


def main():
    obj = Demo()
    print(obj.public_value)
    print(obj._internal_value)       # possible, but client code should respect convention
    print(obj.reveal_private())

    # This name does not exist directly:
    print("Has __private_value:", hasattr(obj, "__private_value"))
    print("Mangled name exists:", hasattr(obj, "_Demo__private_value"))


if __name__ == "__main__":
    main()

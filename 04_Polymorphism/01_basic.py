"""Subtype polymorphism."""

class Animal:
    def speak(self) -> str:
        return "Unknown sound"

class Dog(Animal):
    def speak(self) -> str:
        return "Woof"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow"

def make_it_speak(animal: Animal):
    print(type(animal).__name__, "says", animal.speak())


def main():
    for animal in [Dog(), Cat(), Animal()]:
        make_it_speak(animal)


if __name__ == "__main__":
    main()

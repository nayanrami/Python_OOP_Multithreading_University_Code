"""Simple method overriding."""

class Animal:
    def speak(self):
        return "sound"

class Dog(Animal):
    def speak(self):
        return "woof"

class Cow(Animal):
    def speak(self):
        return "moo"


def main():
    for animal in [Animal(), Dog(), Cow()]:
        print(type(animal).__name__, animal.speak())


if __name__ == "__main__":
    main()

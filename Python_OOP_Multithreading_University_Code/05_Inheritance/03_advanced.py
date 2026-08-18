"""Multiple inheritance and method resolution order (MRO)."""

class Scanner:
    def feature(self):
        return "scan"

class Printer:
    def feature(self):
        return "print"

class AllInOne(Scanner, Printer):
    def features(self):
        return [Scanner.feature(self), Printer.feature(self)]


def main():
    device = AllInOne()
    print(device.features())
    print("MRO:")
    for cls in AllInOne.mro():
        print(" ", cls.__name__)


if __name__ == "__main__":
    main()

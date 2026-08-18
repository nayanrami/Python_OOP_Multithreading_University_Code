"""Supplement: multi-level inheritance."""

class Device:
    def power_on(self):
        return "power on"

class Computer(Device):
    def boot(self):
        return "boot OS"

class Laptop(Computer):
    def portable(self):
        return True

if __name__ == "__main__":
    x = Laptop()
    print(x.power_on(), x.boot(), x.portable())

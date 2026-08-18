"""Supplement: inheritance versus composition."""

class Engine:
    def start(self):
        return "engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has-an Engine

    def start(self):
        return self.engine.start()

if __name__ == "__main__":
    print(Car().start())

"""A payment abstraction hides provider-specific implementation details."""

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

class CardProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:
        return f"Card payment of ₹{amount:.2f} approved"

class UPIProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:
        return f"UPI payment of ₹{amount:.2f} approved"

def checkout(processor: PaymentProcessor, amount: float):
    print(processor.pay(amount))


def main():
    checkout(CardProcessor(), 1250)
    checkout(UPIProcessor(), 499)


if __name__ == "__main__":
    main()

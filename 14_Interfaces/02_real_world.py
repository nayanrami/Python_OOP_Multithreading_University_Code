"""Payment gateway interface."""

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def authorize(self, amount: float) -> bool:
        pass

    @abstractmethod
    def capture(self, amount: float) -> str:
        pass

class CardGateway(PaymentGateway):
    def authorize(self, amount):
        return amount <= 100000

    def capture(self, amount):
        return f"Captured ₹{amount:.2f} by card"

class UPIGateway(PaymentGateway):
    def authorize(self, amount):
        return amount <= 200000

    def capture(self, amount):
        return f"Captured ₹{amount:.2f} by UPI"

def pay(gateway: PaymentGateway, amount: float):
    if gateway.authorize(amount):
        print(gateway.capture(amount))
    else:
        print("Authorization failed")


def main():
    pay(CardGateway(), 5000)
    pay(UPIGateway(), 7500)


if __name__ == "__main__":
    main()

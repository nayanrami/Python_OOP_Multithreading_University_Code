"""Encapsulation using controlled methods."""

class BankAccount:
    def __init__(self, owner: str, opening_balance: float = 0):
        self.owner = owner           # public
        self._balance = 0.0          # internal/protected-by-convention
        self.deposit(opening_balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("withdrawal must be positive")
        if amount > self._balance:
            return False
        self._balance -= amount
        return True

    def get_balance(self) -> float:
        return self._balance


def main():
    account = BankAccount("Kabir", 1000)
    account.deposit(500)
    print("Withdraw 200:", account.withdraw(200))
    print("Balance:", account.get_balance())


if __name__ == "__main__":
    main()

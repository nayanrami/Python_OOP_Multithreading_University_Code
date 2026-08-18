"""Supplement: a read-only identifier with controlled balance."""

class Wallet:
    def __init__(self, wallet_id):
        self._wallet_id = wallet_id
        self.__balance = 0

    @property
    def wallet_id(self):
        return self._wallet_id

    @property
    def balance(self):
        return self.__balance

    def add_money(self, amount):
        if amount <= 0:
            raise ValueError
        self.__balance += amount

if __name__ == "__main__":
    w = Wallet("W01")
    w.add_money(300)
    print(w.wallet_id, w.balance)

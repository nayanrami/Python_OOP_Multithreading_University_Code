"""Encapsulation with a private name-mangled attribute."""

class UserAccount:
    def __init__(self, username: str, pin: str):
        self.username = username
        self.__pin = None
        self.change_pin(pin)

    def change_pin(self, new_pin: str) -> None:
        if not (new_pin.isdigit() and len(new_pin) == 4):
            raise ValueError("PIN must contain exactly four digits")
        self.__pin = new_pin

    def verify_pin(self, candidate: str) -> bool:
        return candidate == self.__pin


def main():
    user = UserAccount("student01", "1234")
    print("Correct:", user.verify_pin("1234"))
    print("Incorrect:", user.verify_pin("9999"))
    user.change_pin("4321")
    print("Changed:", user.verify_pin("4321"))


if __name__ == "__main__":
    main()

"""Supplement: override parent validation."""

class User:
    def role(self):
        return "user"

class Admin(User):
    def role(self):
        return "admin"

if __name__ == "__main__":
    print(User().role(), Admin().role())

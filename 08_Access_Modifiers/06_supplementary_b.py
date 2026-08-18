"""Supplement: private method name mangling."""

class SecurityDemo:
    def public_check(self):
        return self.__internal_check()

    def __internal_check(self):
        return "checked"

if __name__ == "__main__":
    print(SecurityDemo().public_check())

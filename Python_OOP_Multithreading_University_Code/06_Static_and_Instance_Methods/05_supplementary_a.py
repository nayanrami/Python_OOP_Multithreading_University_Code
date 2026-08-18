"""Supplement: utility static method."""

class PasswordRules:
    @staticmethod
    def strong(value):
        return len(value) >= 8 and any(c.isdigit() for c in value)

if __name__ == "__main__":
    print(PasswordRules.strong("abc"))
    print(PasswordRules.strong("python123"))

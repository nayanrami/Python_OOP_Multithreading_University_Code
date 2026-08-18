"""Supplement: public API delegates to internal helper."""

class Validator:
    def validate(self, text):
        return self._not_empty(text) and self._short_enough(text)

    def _not_empty(self, text):
        return bool(text.strip())

    def _short_enough(self, text):
        return len(text) <= 20

if __name__ == "__main__":
    print(Validator().validate("Python"))

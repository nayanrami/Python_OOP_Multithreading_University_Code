"""Supplement: duck typing as an informal interface."""

class JsonSaver:
    def save(self, data):
        return "JSON saved"

class TextSaver:
    def save(self, data):
        return "Text saved"

def persist(saver, data):
    print(saver.save(data))

if __name__ == "__main__":
    persist(JsonSaver(), {"x": 1})
    persist(TextSaver(), "hello")

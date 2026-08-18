"""Supplement: polymorphic file-like writers."""

class ScreenWriter:
    def write(self, text):
        print("SCREEN:", text)

class BufferWriter:
    def __init__(self):
        self.data = []
    def write(self, text):
        self.data.append(text)

def emit(writer, text):
    writer.write(text)

if __name__ == "__main__":
    emit(ScreenWriter(), "hello")
    b = BufferWriter()
    emit(b, "hello")
    print(b.data)

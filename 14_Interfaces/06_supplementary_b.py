"""Supplement: Protocol supports static type checking."""

from typing import Protocol

class Closeable(Protocol):
    def close(self) -> None: ...

class Resource:
    def close(self):
        print("closed")

def finish(resource: Closeable):
    resource.close()

if __name__ == "__main__":
    finish(Resource())

"""Factory class method plus static validation helpers."""

class IPv4Address:
    def __init__(self, octets: tuple[int, int, int, int]):
        if not self.valid_octets(octets):
            raise ValueError("invalid IPv4 octets")
        self.octets = octets

    @classmethod
    def from_string(cls, value: str):
        parts = tuple(int(part) for part in value.split("."))
        return cls(parts)

    @staticmethod
    def valid_octets(octets):
        return len(octets) == 4 and all(0 <= part <= 255 for part in octets)

    def __str__(self):
        return ".".join(map(str, self.octets))


def main():
    ip = IPv4Address.from_string("192.168.1.10")
    print(ip)
    print(IPv4Address.valid_octets((8, 8, 8, 8)))


if __name__ == "__main__":
    main()

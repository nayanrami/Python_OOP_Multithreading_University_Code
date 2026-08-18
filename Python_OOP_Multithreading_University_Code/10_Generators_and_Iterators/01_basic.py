"""Generator function with yield."""

def even_numbers(limit: int):
    number = 0
    while number <= limit:
        yield number
        number += 2


def main():
    generator = even_numbers(10)
    print("Generator object:", generator)
    for value in generator:
        print(value, end=" ")
    print()


if __name__ == "__main__":
    main()

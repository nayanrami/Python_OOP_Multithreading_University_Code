"""LeetCode 1603-inspired: Design Parking System.

Focus: storing object state and updating it through methods.
"""

class ParkingSystem:
    BIG, MEDIUM, SMALL = 1, 2, 3

    def __init__(self, big: int, medium: int, small: int):
        self.capacity = {
            self.BIG: big,
            self.MEDIUM: medium,
            self.SMALL: small,
        }

    def addCar(self, carType: int) -> bool:
        if self.capacity.get(carType, 0) == 0:
            return False
        self.capacity[carType] -= 1
        return True


def main():
    parking = ParkingSystem(big=1, medium=1, small=0)
    for car_type in [1, 2, 3, 1]:
        print(car_type, "->", parking.addCar(car_type))


if __name__ == "__main__":
    main()

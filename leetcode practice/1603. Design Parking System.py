class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int):
        if carType == 1 and self.big==0:
            return False
        elif carType == 2 and self.medium==0:
            return False
        elif carType == 3 and self.small==0:
            return False

        if carType == 1:
            self.big -= 1
        elif carType == 2:
            self.medium -= 1
        elif carType == 3:
            self.small -= 1
        return True
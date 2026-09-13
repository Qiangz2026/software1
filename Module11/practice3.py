#Multiple inheritance
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class SportsItem:
    def __init__(self, weight):
        self.weight = weight

class Bicycle(Vehicle, SportsItem):
    def __init__(self, speed, weight, gears):
        #In multiple inheritance, cannot call the base class initializer this way.
        # super().__init__(speed)
        # super().__init__(weight) 
        Vehicle.__init__(self, speed)#To call a base class's initializer directly using the base class name, need to pass `self` as an argument.
        SportsItem.__init__(self, weight)
        self.gears = gears

b = Bicycle(45, 18.7, 3)
print(b.gears)
print(b.speed)
print(b.weight)


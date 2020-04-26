class Car:
    wheels = 4
    def __init__(self):
        self.mil = 10
        self.company = "BMW"

c1 = Car()
c2 = Car()
c1.mil = 55
Car.wheels = 5
print(c1.company, c1.mil, c1.wheels)
print(c2.company, c2.mil, c2.wheels)
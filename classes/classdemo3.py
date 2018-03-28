"""
Object Oriented Programming
"""


class CarDemo(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car: " + self.make)
        print("Model of the car: " + self.model)


c1 = CarDemo('bmw', '550i')
c1.info()
c1.wheels = 3
print(c1.wheels)

c2 = CarDemo('benz', 'c500')
c2.info()
print(c2.wheels)

print(CarDemo.wheels)
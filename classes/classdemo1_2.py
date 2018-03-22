"""
Object Oriented Programming
"""


class CarDemo(object):

    def __init__(self, make, model="550i"):
        self.make = make
        self.model = model
c1 = CarDemo('bmw')
print(c1.make)
print(c1.model)

c2 = CarDemo('benz', 'c500')
print(c2.make)
print(c2.model)
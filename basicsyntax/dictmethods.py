"""
Dictionary Methods bla bla 
"""
car = {'make': 'bmw', 'model': '550i', "year": 2016}
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}

print(car.keys())
print(cars.keys())

print("*"*20)
print(car.values())
print(cars.values())

print("*"*20)
print(car.items())
print(cars.items())

print("*"*20)
car_copy = car.copy()
print(car_copy)

print("*"*20)
print(car.pop('model'))
print(car)

print("*"*20)
car.clear()
print(car)

print("*"*20)


cars = ["bmw", "honda", "audi"]

length = len(cars)
print(length)

cars.append("benz")
print(cars)

cars.insert(1, "jeep")
print(cars)

x = cars.index("honda")
print(x)

y = cars.pop()
print(y)
print(cars)

cars.remove("jeep")
print(cars)

slicing = cars[0:2]
print(slicing)
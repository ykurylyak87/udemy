"""
Built-in function
Creates a sequence of numbers but does not save them in memory
Very useful for generating numbers
"""


print(list(range(0, 10, 2)))

a = range(0, 10)
print(list(a))
print(type(a))

for num in range(1, 4):
    print(num)

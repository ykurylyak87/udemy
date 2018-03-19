"""
Tuple
Like list but they are immutable
It means you can't change them
"""

my_list = [1, 2, 3]
print(my_list)

print("*"*20)
my_list[0] = 0
print(my_list)

print("*"*20)
my_tuple = (1, 2, 3)
# my_tuple[0] = 0 -> you can't do like this! Tuple doesn't support item assignment
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1:])

print("*"*20)
print("Index of 2 in tuple -> " + str(my_tuple.index(2)))

print("*"*20)
my_tuple = (1, 2, 3, 4, 5, 6, 7, 1, 1)
print("Count how many '1' are in tuple -> " + str(my_tuple.count(1)))

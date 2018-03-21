"""
Some built-in functions
max(): It takes any number of arguments and returns the largest one.

min(): It takes any number of arguments and returns the smallest one.

abs(): It returns the absolute value of the number, that number's distance from 0.
It always returns a positive value and it only takes a single number.

type(): It returns the type of the data it receives as an argument.
"""


def largest_num(*args):
    # print(max(args))
    return max(args)


def smallest_num(*args):
    return min(args)


def abs_function(a):
    return abs(a)

x = largest_num(-20, -10, 0, 10, 100)
print('The largest number is ' + str(x))

x = smallest_num(-20, -10, 0, 10, 100)
print('The smallest number is ' + str(x))

x = abs_function(30)
print('Absolute value of number is ' + str(x))

x = abs_function(-30)
print('Absolute value of number is ' + str(x))

print(type(99))
print(type(99.9))
print(type("99.9"))

l = [1, 2, 3]
print(type(l))

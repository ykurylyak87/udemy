"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from outside
"""


def sum_nums(a=2, b=4):
    """
    Get sum of two numbers
    :param a:
    :param b:
    :return:
    """
    return a + b

c = sum_nums(b=6, a=8)
print(c)

z = sum_nums(b=5)
print(z)
def sum_nums(a, b):
    """
    Get sum of two numbers
    :param a:
    :param b:
    :return:
    """
    return a + b

c = sum_nums(5, 5)
print(c)


def is_metro(city):
    l = ['sfo', 'nyc', 'la']
    if city in l:
        return True
    else:
        return False


x = is_metro('sfo')
print(x)

y = is_metro(input("Input a city name: "))
print(y)

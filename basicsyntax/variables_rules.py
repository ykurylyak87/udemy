"""
variables rules
"""
import keyword

# this will print a list of keywords
print(keyword.kwlist)
print(10 * "*")

# this will print a list of keywords each one from the new line
for x in keyword.kwlist:
    print(x)
print(10 * "*")

# another way to print list every string from a new line
print('\n'.join(keyword.kwlist))
print(10 * "*")

a = b = c = 10
print(a)
print(b)
print(c)

x, y, z = 10, 20, 30
print(x)
print(y)
print(z)

"""
Break: To break out of the closest enclosing loop
Continue: Go to the start of the closest enclosing loop
"""

x = 0
while x < 10:
    print('Value of x is: ' + str(x))
    x += 1

    if x == 8:
        break
    print("*" * x)

print('*' * 20)

y = 0
while y < 10:
    print('Value of x is: ' + str(y))
    y += 1

    if y == 8:
        continue
    print("*" * y)

print('*' * 20)

z = 0
while z < 10:
    print('Value of x is: ' + str(z))
    z += 1
    print("*" * z)
else:
    print("Finished!")
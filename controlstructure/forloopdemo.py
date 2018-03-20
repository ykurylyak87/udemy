"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""

# String for loop
my_string = 'abcabc'

for c in my_string:
    if c == 'a':
        print('A', end=' ')
    else:
        print(c, end=' ')

print('\n' + '*' * 20)

# List for loop
cars = ['bmw', 'benz', 'honda']

for car in cars:
    print(car)

print('*' * 20)

nums = [1, 2, 3]
for n in nums:
    print(n * 10)

print('*' * 20)

# Dictionary fo loop
d = {'one': 1, 'two': 2, 'three': 3}
for key in d:
    print(key + ' ' + str(d[key]))

print('*' * 20)
for k, v in d.items():
    print(k)
    print(v)
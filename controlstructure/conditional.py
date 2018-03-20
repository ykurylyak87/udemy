"""
Conditional Logic
"""

if 100 > 10:
    print("100 is greater than 10")

value = input("Input: red, yellow or green: \n-> ")

if value == 'green':
    print('Go')
elif value == 'yellow':
    print('Prepare to stop')
else:
    print('Stop')
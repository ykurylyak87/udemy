"""
and
**************************************
True and True   --> True
True and False  --> False
False and False --> False
**************************************

or
**************************************
True or True   --> True
True or False  --> True
False or False --> False
**************************************

not
**************************************
Not True  --> False
Not False --> True
"""

print("---AND---")
print("*"*10)
and_output1 = (10 == 10) and (10 > 9)
print(and_output1)

print("*"*10)
and_output2 = (10 == 10) and (10 < 9)
print(and_output2)

print("*"*10)
and_output3 = (10 > 10) and (10 < 9)
print(and_output3)
print("*"*10)

print("---OR---")
print("*"*10)
or_output1 = (10 == 10) or (10 > 9)
print(or_output1)
print("*"*10)
or_output2 = (10 == 10) or (10 < 9)
print(or_output2)
print("*"*10)
or_output3 = (10 > 10) or (10 < 9)
print(or_output3)
print("*"*10)
print("---NOT---")
print("*"*10)
not_true = not (10 == 10)
print(not_true)
print("*"*10)
not_false = not (10 > 10)
print(not_false)
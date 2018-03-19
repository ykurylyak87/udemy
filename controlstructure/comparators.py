"""
== --> value equality
!= --> not equal to
<  --> less than
>  --> greater than
<= --> less than or equal to
>= --> greater than or equal to
"""

bool_one = 10 == 10
print(bool_one)

print("*"*20)
bool_one = 10 == 11
print(bool_one)

print("*"*20)
not_equal = 10 != 10
print(not_equal)

print("*"*20)
less_than = 10 < 10
print(less_than)

print("*"*20)
greater_than = 10 > 10
print(greater_than)

print("*"*20)
lt_eq = 10 <= 10
print(lt_eq)
lt_eq = 10 <= 9
print(lt_eq)

print("*"*20)
gt_eq = 10 >= 11
print(gt_eq)
gt_eq = 10 >= 10
print(gt_eq)
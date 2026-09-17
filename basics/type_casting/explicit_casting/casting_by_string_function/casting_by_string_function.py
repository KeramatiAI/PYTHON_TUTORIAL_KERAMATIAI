"""
# CASTING BY STRING FUNCTION str() ****************************
"""

# Integer to string
var_string_1 = str(10)
print(type(var_string_1))
print(var_string_1)

# Float to String
var_string_2 = str(11.10)
print(type(var_string_2))
print(var_string_2)

var_string_3 = str(2 / 5)
print(type(var_string_3))
print(var_string_3)

# Floating points in scientific notations using E or e and with positive or negative power are converted to string with str() function.
var_string_4 = str(10E4)
print(type(var_string_4))
print(var_string_4)

var_string_5 = str(1.23e-4)
print(type(var_string_5))
print(var_string_5)
"""
When Boolean constant is entered as argument, it is surrounded by (') so that True becomes 'True'. 
List and Tuple objects can also be given argument to str() function. The resultant string is the list/tuple surrounded by (').
"""
var_string_6 = str('True')
print(type(var_string_6))
print(var_string_6)

var_string_7 = str([1, 2, 3])
print(type(var_string_7))
print(var_string_7)

var_string_8 = str((1, 2, 3))
print(type(var_string_8))
print(var_string_8)

var_string_9 = str({1: 100, 2: 200, 3: 300})
print(type(var_string_9))
print(var_string_9)

# Following is an example to convert number, float and string into string data type:
a = str(1)  # a will be "1"
b = str(2.2)  # b will be "2.2"
c = str("3.3")  # c will be "3.3"

print(a)
print(b)
print(c)

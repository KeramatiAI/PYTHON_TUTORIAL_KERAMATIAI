"""
# CASTING BY STRING FUNCTION str() ****************************
"""

# Integer to string
var_string_1 = str(10)
print(type(var_string_1))
print(var_string_1)

# Float to String
var_string_2 =str(11.10)
print(type(var_string_2))
print(var_string_2)

var_string_3 = str(2/5)
print(type(var_string_3))
print(var_string_3)

# Floating points in scientific notations using E or e and with positive or negative power are converted to string with str() function.
var_string_4 = str(10E4)
print(type(var_string_4))
print(var_string_4)

var_string_5 = str(1.23e-4)
print(type(var_string_5))
print(var_string_5)
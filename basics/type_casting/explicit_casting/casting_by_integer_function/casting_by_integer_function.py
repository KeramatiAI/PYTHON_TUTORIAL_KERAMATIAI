"""
# CASTING BY INTEGER FUNCTION ****************************
1-Python int() Function
Python's built-in int() function converts an integer literal to an integer object, a float to integer, and
a string to integer if the string itself has a valid integer literal representation.
"""
a = int(10)
b = a

print(type(b))

print("#######################################")
c = int(10.5) #converts a float object to int
d = int(2*3.14) #expression results float, is converted to int

print(type(c))
print(type(d))

print("#######################################")

e = int(True)

print(type(e))

print("#######################################")

f = int("100")

print(type(f))

g = ("10"+"01")
g = int("10"+"01")

print(type(g))
print("#######################################")
"""
2-String to Integer
The int() function returns an integer from a string object, only if it contains a valid integer representation.
"""
h = int("100")
print(type(h))

i = ("10"+"01")
i = int("10"+"01")

type(i)
print("#######################################")
# j = int("10.5") #ValueError: invalid literal for int() with base 10: '10.5'
# k = int("Hello World")#ValueError: invalid literal for int() with base 10: 'Hello World'
print("#######################################")
"""
Binary String to Integer
The string should be made up of 1 and 0 only, and the base should be 2.
"""
l = int("110011", 2)
print(l)
"""
The Decimal equivalent of binary number 110011 is 51.
"""
print("#######################################")
"""
Octal String to Integer
The string should only contain 0 to 7 digits, and the base should be 8.
"""
m = int("20", 8)
print(m)
"""
The Decimal equivalent of octal 20 is 16.
"""
print("#######################################")
"""
Hexa-Decimal String to Integer
The string should contain only the Hexadecimal symbols i.e., 0-9 and A, B, C, D, E or F. Base should be 16.
"""
var_hexa = int("2A9", 16)
print(var_hexa)
"""
Decimal equivalent of Hexadecimal 2A9 is 681. You can easily verify these conversions with calculator app in Windows, Ubuntu or Smartphones.

Following is an example to convert number, float and string into integer data type:
"""
var_integer1 = int(1)     # a will be 1
var_integer2 = int(2.2)   # b will be 2
var_integer3 = int("3")   # c will be 3

print (var_integer1)
print (var_integer2)
print (var_integer3)


"""
Python int() Function
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



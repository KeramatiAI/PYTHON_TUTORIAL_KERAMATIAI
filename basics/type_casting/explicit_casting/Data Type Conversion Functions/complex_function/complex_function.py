"""
Syntax:
complex(real [,imag])
"""

"""
Parameters
This function takes two optional parameters as shown below −

real − It represents the real part of the complex number. If not provided, it defaults to 0.

imag (optional) − It represents the imaginary part of the complex number. If not provided, it defaults to 0.

Return Value
This function returns a complex number based on the provided real and imaginary parts or a string representing a complex number.
"""

# example 1
real = 2
imaginary = 3
result = complex(real, imaginary)
print('The complex value obtained is:', result)
print(type(result))

# example 2
real = 4
result = complex(real)
print('The complex value obtained is:', result)
print(type(result))

# example 3
imaginary = 7
result = complex(imag=imaginary)
print('The complex value obtained is:', result)
print(type(result))

# example 4
result = complex()
print('The complex value obtained is:',result)
print(type(result))

# example 5
result = complex("2+4j")
print('The complex value obtained is:',result)
print(type(result))

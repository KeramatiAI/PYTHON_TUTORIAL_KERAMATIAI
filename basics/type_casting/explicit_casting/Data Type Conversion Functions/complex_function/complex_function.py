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
real = 2
imaginary = 3
result = complex(real, imaginary)
print('The complex value obtained is:',result)
print(type(result))
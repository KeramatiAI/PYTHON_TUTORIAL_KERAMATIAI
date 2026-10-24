"""
Python defines ":" as string slicing operator. It returns a substring from the original string. Its general usage is as follows −

substr=var[x:y]
The ":" operator needs two integer operands (both of which may be omitted, as we shall see in subsequent examples).
The first operand x is the index of the first character of the desired slice.
The second operand y is the index of the character next to the last in the desired string. So var(x:y] separates characters from xth position to (y-1)th position from the original string.
"""
var="HELLO PYTHON"

print ("var:",var)
print ("var[3:8]:", var[3:8])
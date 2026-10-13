"""
Python Bitwise Left Shift Operator (<<)
Left shift operator shifts most significant bits to right by the number on the right side of the "<<" symbol. Hence, "x << 2" causes two bits of the binary representation of to right.
"""
a=60
print ("a:",a, "a<<2:", a<<2)
"""
How does this take place? Let us use the binary equivalent of 60, and perform the left shift by 2.

0011 1100
<<
    2
-------------
1111 0000
"""
print(int('11110000',2))
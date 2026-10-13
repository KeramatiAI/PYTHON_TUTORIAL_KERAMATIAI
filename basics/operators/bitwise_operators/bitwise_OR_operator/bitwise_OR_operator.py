"""
The "|" symbol (called pipe) is the bitwise OR operator. If any bit operand is 1, the result is 1 otherwise it is 0.

0 | 0 is 0
0 | 1 is 1
1 | 0 is 1
1 | 1 is 1
"""
a=60
b=13
print ("a:",a, "b:",b, "a|b:",a|b)
print ("a:", bin(a))
print ("b:", bin(b))
"""
It will produce the following output −

a: 60 b: 13 a|b: 61
a: 0b111100
b: 0b1101
To perform the "|" operation manually, use the 8-bit format.

0011 1100
    |
0000 1101
-------------
0011 1101
Convert the binary number back to integer to tally the result −
"""
print(int('00111101',2))
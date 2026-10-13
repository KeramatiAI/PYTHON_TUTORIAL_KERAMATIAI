"""
The term XOR stands for exclusive OR. It means that the result of OR operation on two bits will be 1 if only one of the bits is 1.

0 ^ 0 is 0
0 ^ 1 is 1
1 ^ 0 is 1
1 ^ 1 is 0
"""
a=60
b=13
print ("a:",a, "b:",b, "a^b:",a^b)
"""
It will produce the following output −

a: 60 b: 13 a^b: 49
We now perform the bitwise XOR manually.

0011 1100
    ^
0000 1101
-------------
0011 0001
The int() function shows 00110001 to be 49.
"""
print(int('00110001',2))

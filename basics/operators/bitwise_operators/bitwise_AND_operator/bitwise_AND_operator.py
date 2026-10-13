"""
Bitwise AND operator is somewhat similar to logical and operator. It returns True only if both the bit operands are 1 (i.e. True). All the combinations are −

0 & 0 is 0
1 & 0 is 0
0 & 1 is 0
1 & 1 is 1

When you use integers as the operands, both are converted in equivalent binary, the & operation is done on corresponding bit from each number, starting from the least significant bit and going towards most significant bit.
"""
a=60
b=13
print ("a:",a, "b:",b, "a&b:",a&b)

"""
To understand how Python performs the operation, obtain the binary equivalent of each variable.
"""
print ("a:", bin(a))
print ("b:", bin(b))

"""
It will produce the following output −

a: 0b111100
b: 0b1101
For the sake of convenience, use the standard 8-bit format for each number, so that "a" is 00111100 and "b" is 00001101. Let us manually perform and operation on each corresponding bits of these two numbers.

0011 1100
&
0000 1101
-------------
0000 1100
Convert the resultant binary back to integer. You'll get 12, which was the result obtained earlier.
"""
print(int('00001100',2))

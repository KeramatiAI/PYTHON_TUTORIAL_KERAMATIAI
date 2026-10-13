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

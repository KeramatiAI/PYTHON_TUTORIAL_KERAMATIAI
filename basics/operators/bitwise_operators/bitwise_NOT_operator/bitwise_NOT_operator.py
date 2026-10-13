"""
This operator is the binary equivalent of logical NOT operator. It flips each bit so that 1 is replaced by 0, and 0 by 1, and returns the complement of the original number. Python uses 2's complement method. For positive integers, it is obtained simply by reversing the bits. For negative number, -x, it is written using the bit pattern for (x-1) with all of the bits complemented (switched from 1 to 0 or 0 to 1). Hence: (for 8 bit representation)

-1 is complement(1 - 1) = complement(0) = "11111111"
-10 is complement(10 - 1) = complement(9) = complement("00001001") = "11110110".
"""
a=60
print ("a:",a, "~a:", ~a)


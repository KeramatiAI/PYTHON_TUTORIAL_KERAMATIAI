"""
Python Bitwise Right Shift Operator (>>)
Right shift operator shifts least significant bits to left by the number on the right side of the ">>" symbol. Hence, "x >> 2" causes two bits of the binary representation of to left.
"""
a=60
print ("a:",a, "a>>2:", a>>2)
"""
Manual right shift operation on 60 is shown below −

 0011 1100
   >>
   2
   -------------
   0000 1111
"""
#Use int() function to covert the above binary number to integer. It is 15.
print(int('00001111',2))
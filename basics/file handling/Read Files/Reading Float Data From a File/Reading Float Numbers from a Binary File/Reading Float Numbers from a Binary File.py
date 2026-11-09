"""
Reading Float Numbers from a Binary File
To read floating-point data from a binary file, we use the struct.unpack() method to convert the bytes object back into a float −
"""
import struct

# Open the file in binary read mode
with open('test.bin', 'rb') as f:
   # Read the binary data from the file
   data = f.read()

   # Unpack the binary data to retrieve the float
   x = struct.unpack('f', data)[0]

   # Print the float value
   print(x)

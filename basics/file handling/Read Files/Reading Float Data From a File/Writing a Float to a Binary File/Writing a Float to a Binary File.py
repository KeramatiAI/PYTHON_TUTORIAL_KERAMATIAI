"""
Writing a Float to a Binary File
To write floating-point data to a binary file, we use the struct.pack() method to convert the float into a bytes object −
"""
import struct

# Define a floating-point number
x = 23.50

# Pack the float into a binary format
data = struct.pack('f', x)

# Open the file in binary write mode and write the packed data
with open('test.bin', 'wb') as f:
   f.write(data)

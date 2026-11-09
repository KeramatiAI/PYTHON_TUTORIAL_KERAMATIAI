"""
Writing an Integer to a Binary File
Following is an example on how to write an integer to a binary file −
"""
# Convert the integer to bytes and write to a binary file
n = 25
data = n.to_bytes(8, 'big')

with open('test.bin', 'wb') as f:
   f.write(data)

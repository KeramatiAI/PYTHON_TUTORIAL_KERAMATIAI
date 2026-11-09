"""
Reading an Integer from a Binary File
To read back the integer data from the binary file, convert the output of the read() function back to an integer using the from_bytes() method −
"""
# Read the binary data from the file and convert it back to an integer
with open('test.bin', 'rb') as f:
   data = f.read()
   n = int.from_bytes(data, 'big')
   print(n)


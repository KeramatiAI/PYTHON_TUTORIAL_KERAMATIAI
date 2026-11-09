"""
Converting Text Strings to Bytes
Conversion of a text string to bytes can be done using the encode() function. This is useful when you need to write text data as binary data −
"""
# Open a file in binary write mode
with open('test.bin', 'wb') as f:
   # Convert text string to bytes
   data = "Hello World".encode('utf-8')
   f.write(data)


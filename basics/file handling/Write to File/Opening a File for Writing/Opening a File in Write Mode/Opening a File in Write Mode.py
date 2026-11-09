"""
Opening a File in Write Mode
This mode is used when you want to write data to a file, starting from scratch each time the file is opened −
"""
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()
print ("File opened successfully!!")
"""
Following is the output obtained −

File opened successfully!!
"""
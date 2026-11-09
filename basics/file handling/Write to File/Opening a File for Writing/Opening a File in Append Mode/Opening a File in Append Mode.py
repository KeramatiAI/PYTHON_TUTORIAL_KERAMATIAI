"""
Opening a File in Append Mode
This mode is used when you want to add data to the end of the file without altering its existing contents −
"""
file = open("example.txt", "a")
file.write("Appending this line.\n")
file.close()
print ("File opened successfully!!")
"""
This will produce the following result −

File opened successfully!!
"""
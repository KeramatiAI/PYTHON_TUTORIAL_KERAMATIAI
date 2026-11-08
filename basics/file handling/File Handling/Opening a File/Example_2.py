"""
Example 2
In here, we are opening a file named "foo.txt" in binary write mode ("wb"), printing its name, whether it's closed, and its opening mode, and then closing the file −
"""
# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not: ", fo.closed)
print ("Opening mode: ", fo.mode)
fo.close()
"""
It will produce the following output −

Name of the file: foo.txt
Closed or not: False
Opening mode: wb
"""
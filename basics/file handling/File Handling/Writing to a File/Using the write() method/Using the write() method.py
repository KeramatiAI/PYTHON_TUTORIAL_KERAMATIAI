"""
Using the write() method
In this example, we are using the write() method to write the string passed to it to the file. If the file is opened in 'w' mode, it will overwrite any existing content. If the file is opened in 'a' mode, it will append the string to the end of the file −
"""
with open("foo.txt", "w") as file:
   file.write("Hello, World!")
   print ("Content added Successfully!!")
"""
Output of the above code is as follows −

Content added Successfully!!
"""
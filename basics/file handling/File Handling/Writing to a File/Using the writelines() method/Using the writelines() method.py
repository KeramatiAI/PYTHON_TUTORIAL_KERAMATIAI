"""
Using the writelines() method
In here, we are using the writelines() method to take a list of strings and writes each string to the file. It is useful for writing multiple lines at once −
"""
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("example.txt", "w") as file:
   file.writelines(lines)
   print ("Content added Successfully!!")
"""
The result obtained is as follows −

Content added Successfully!!
"""
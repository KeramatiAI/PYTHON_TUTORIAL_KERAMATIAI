"""
Using read() method
In the following example, we are using the read() method to read the whole file into a single string −
"""
with open("example.txt", "r") as file:
   content = file.read()
   print(content)
"""
Following is the output obtained −

Hello!!!
Welcome to TutorialsPoint!!!
"""
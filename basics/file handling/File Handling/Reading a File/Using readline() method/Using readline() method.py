"""
Using readline() method
In here, we are using the readline() method to read one line at a time, making it memory efficient for reading large files line by line −
"""
with open("example.txt", "r") as file:
   line = file.readline()
   while line:
      print(line, end='')
      line = file.readline()
"""
Output of the above code is as shown below −

Hello!!!
Welcome to TutorialsPoint!!!
"""
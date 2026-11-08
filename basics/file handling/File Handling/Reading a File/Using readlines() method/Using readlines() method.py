"""
Using readlines() method
Now, we are using the readlines() method to read the entire file and splits it into a list where each element is a line −
"""
with open("example.txt", "r") as file:
   lines = file.readlines()
   for line in lines:
      print(line, end='')
"""
We get the output as follows −

Hello!!!
Welcome to TutorialsPoint!!!
"""
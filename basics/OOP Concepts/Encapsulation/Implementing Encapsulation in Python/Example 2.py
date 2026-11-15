"""
Example 2
Let us modify the Student class. Add another instance variable salary. Make name private and marks as private by prefixing double underscores to them.
"""
class Student:

   def __init__(self, name="Rajaram", marks=50):
      self.__name = name
      self.__marks = marks
   def studentdata(self):
      print ("Name: {} marks: {}".format(self.__name, self.__marks))

s1 = Student()
s2 = Student("Bharat", 25)

s1.studentdata()
s2.studentdata()
print ("Name: {} marks: {}".format(s1.__name, s2.__marks))
print ("Name: {} marks: {}".format(s2.__name, __s2.marks))
"""
When you run this code, it will produce the following output −

Name: Rajaram marks: 50
Name: Bharat marks: 25
Traceback (most recent call last):
 File "C:\Python311\hello.py", line 14, in <module>
  print ("Name: {} marks: {}".format(s1.__name, s2.__marks))
AttributeError: 'Student' object has no attribute '__name'
The above output makes it clear that the instance variables name and age, can be accessed by a method declared inside the class (the studentdata() method), but the double underscores prefix makes the variables private, and hence, accessing them outside the class is restricted which raises Attribute error.
"""
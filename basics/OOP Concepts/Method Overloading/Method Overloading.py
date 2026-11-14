"""
Method overloading is a feature of object-oriented programming where a class can have multiple methods with the same name but different parameters. To overload method, we must change the number of parameters or the type of parameters, or both.

Method Overloading in Python
Unlike other programming languages like Java, C++, and C#, Python does not support the feature of method overloading by default. However, there are alternative ways to achieve it.

Example
If you define a method multiple times as shown in the below code, the last definition will override the previous ones. Therefore, this way of achieving method overloading in Python generates error.
"""
class example:
   def add(self, a, b):
      x = a+b
      return x
   def add(self, a, b, c):
      x = a+b+c
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))
"""
The first call to add() method with three arguments is successful. However, calling add() method with two arguments as defined in the class fails.

60
Traceback (most recent call last):
 File "C:\Users\user\example.py", line 12, in <module>
  print (obj.add(10,20))
         ^^^^^^^^^^^^^^
TypeError: example.add() missing 1 required positional argument: 'c'
The output tells you that Python considers only the latest definition of add() method, discarding the earlier definitions.

To simulate method overloading, we can use a workaround by defining default value to method arguments as None, so that it can be used with one, two or three arguments.
"""
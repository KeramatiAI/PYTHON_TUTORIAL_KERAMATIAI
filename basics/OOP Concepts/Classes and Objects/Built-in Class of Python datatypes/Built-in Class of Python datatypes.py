"""
Built-in Class of Python datatypes
As mentioned earlier, Python follows object-oriented programming paradigm. Entities like strings, lists and data types belongs to one or another built-in class.

If we want to see which data type belongs to which built-in class, we can use the Python type() function. This function accepts a data type and returns its corresponding class.

Example
The below example demonstrates how to check built-in class of a given data type.
"""
num = 20
print (type(num))
num1 = 55.50
print (type(num1))
s = "TutorialsPoint"
print (type(s))
dct = {'a':1,'b':2,'c':3}
print (type(dct))
def SayHello():
   print ("Hello World")
   return
print (type(SayHello))
"""
When you execute this code, it will display the corresponding classes of Python data types −

<class 'int'>
<class 'float'>
<class 'str'>
<class 'dict'>
<class 'function'>
"""
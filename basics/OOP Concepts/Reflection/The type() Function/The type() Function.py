"""
The type() Function
We have used this function many times. It tells you which class an object belongs to.

Example
Following statements print the respective class of different built-in data type objects
"""
print (type(10))
print (type(2.56))
print (type(2+3j))
print (type("Hello World"))
print (type([1,2,3]))
print (type({1:'one', 2:'two'}))
"""
Here, you will get the following output −

<class 'int'>
<class 'float'>
<class 'complex'>
<class 'str'>
<class 'list'>
<class 'dict'>
Let us verify the type of an object of a user-defined class −
"""
class test:
   pass

obj = test()
print (type(obj))
"""
It will produce the following output −

<class '__main__.test'>
"""
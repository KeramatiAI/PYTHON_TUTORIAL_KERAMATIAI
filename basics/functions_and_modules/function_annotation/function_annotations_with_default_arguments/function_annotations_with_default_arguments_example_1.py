"""
Function Annotations With Default Arguments
If you want to specify a default argument along with the annotation, you need to put it after the annotation expression. Default arguments must come after the required arguments in the argument list.

Example 1
The following example demonstrates how to provide annotation for default arguments of a function.
"""
def myfunction(a: "physics", b:"Maths" = 20) -> int:
   c = a+b
   return c
print (myfunction(10))
"""
The function in Python is also an object, and one of its attributes is __annotations__. You can check with dir() function.
"""
print (dir(myfunction))
"""
This will print the list of myfunction object containing __annotations__ as one of the attributes.

['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
"""
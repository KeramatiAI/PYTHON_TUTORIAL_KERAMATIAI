"""
Listing All the Tuple Methods
To explore all available methods for tuples, you can utilize the Python dir() function, which lists all properties and functions related to a class. Additionally, the help() function provides detailed documentation for each method. Here's an exampl:
"""
print(dir((1, 2)))
print(help((1, 2).index))
"""
The above code snippet provides a complete list of properties and functions related to the tuple class. It also demonstrates how to access detailed documentation for a specific method in your Python environment. Here is the output −

['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
Help on built-in function index:

index(value, start=0, stop=9223372036854775807, /) method of builtins.tuple inst ance
    Return first index of value.
    
    Raises ValueError if the value is not present.
(END
"""


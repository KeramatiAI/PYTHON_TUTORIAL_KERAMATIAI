"""
Conversion of Sequence Types
List, Tuple and String are Python's sequence types. They are ordered or indexed collection of items.

A string and tuple can be converted into a list object by using the list() function. Similarly, the tuple() function converts a string or list to a tuple.

We shall take an object each of these three sequence types and study their inter-conversion.
"""
a=[1,2,3,4,5]   # List Object
b=(1,2,3,4,5)   # Tupple Object
c="Hello"       # String Object

### list() separates each character in the string and builds the list
obj=list(c)
print(obj)

### The parentheses of tuple are replaced by square brackets
obj=list(b)
print(obj)

### tuple() separates each character from string and builds a tuple of characters
obj=tuple(c)
print(obj)

### square brackets of list are replaced by parentheses.
obj=tuple(a)
print(obj)

### str() function puts the list and tuple inside the quote symbols.
obj=str(a)
print(obj)

obj=str(b)
print(obj)
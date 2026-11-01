"""
Add Set Items Using the add() Method
The add() method in Python is used to add a single element to the set. It modifies the set by inserting the specified element if it is not already present. If the element is already in the set, the add() method has no change in the set.

Syntax
Following is the syntax to add an element to a set −

set.add(obj)
Where, obj is an object of any immutable type.

In the following example, we are initializing an empty set called "language" and adding elements to it using the add() method −
"""
# Defining an empty set
language = set()

# Adding elements to the set using add() method
language.add("C")
language.add("C++")
language.add("Java")
language.add("Python")

# Printing the updated set
print("Updated Set:", language)
"""
It will produce the following output −

Updated Set: {'Python', 'Java', 'C++', 'C'}
"""
"""
Sets in Python are unordered collections of unique elements, often used for membership testing and eliminating duplicates. Set objects support various mathematical operations like union, intersection, difference, and symmetric difference. The set class includes several built-in methods that allow you to add, update, and delete elements efficiently, as well as to perform various set operations such as union, intersection, difference, and symmetric difference on elements.

Understanding Set Methods
The set methods provide convenient ways to manipulate sets, allowing users to add or remove elements, perform set operations, and check for membership and relationships between sets. You can view all available methods for sets, using the Python dir() function to list all properties and functions related to the set class. Additionally, the help() function provides detailed documentation for each method.

Python Set Methods
Below are the built-in methods for sets in Python, categorized based on their functionality. Let's explore and understand the basic functionality of each method.

Adding and Removing Elements
The following are the methods specifically designed for adding and removing item/items into a set −

Sr.No.	Methods with Description
1
set.add()

Add an element to a set.

2
set.clear()

Remove all elements from a set.

3
set.copy()

Return a shallow copy of a set.

4
set.discard()

Remove an element from a set if it is a member.

5
set.pop()

Remove and return an arbitrary set element.

6
set.remove()

Remove an element from a set; it must be a member.

Set Operations
These methods perform set operations such as union, intersection, difference, and symmetric difference −

Sr.No.	Methods with Description
1
set.update()

Update a set with the union of itself and others.

2
set.difference_update()

Remove all elements of another set from this set.

3
set.intersection()

Returns the intersection of two sets as a new set.

4
set.intersection_update()

Updates a set with the intersection of itself and another.

5
set.isdisjoint()

Returns True if two sets have a null intersection.

6
set.issubset()

Returns True if another set contains this set.

7
set.issuperset()

Returns True if this set contains another set.

8
set.symmetric_difference()

Returns the symmetric difference of two sets as a new set.

9
set.symmetric_difference_update()

Update a set with the symmetric difference of itself and another.

10
set.union()

Returns the union of sets as a new set.

11
set.difference()

Returns the difference of two or more sets as a new set.
"""
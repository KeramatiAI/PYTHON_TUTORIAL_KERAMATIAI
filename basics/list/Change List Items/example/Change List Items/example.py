"""
Change List Items
List is a mutable data type in Python. It means, the contents of list can be modified in place, after the object is stored in the memory. You can assign a new value at a given index position in the list

Syntax
list1[i] = newvalue
Example
In the following code, we change the value at index 2 of the given list.
"""
list3 = [1, 2, 3, 4, 5]
print ("Original list ", list3)
list3[2] = 10
print ("List after changing value at index 2: ", list3)
"""
It will produce the following output −

Original list [1, 2, 3, 4, 5]
List after changing value at index 2: [1, 2, 10, 4, 5]
"""
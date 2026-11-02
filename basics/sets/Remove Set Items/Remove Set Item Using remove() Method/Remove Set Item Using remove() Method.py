"""
The remove() method in Python is used to remove the first occurrence of a specified item from a set.

We can remove set items using the remove() method by specifying the element we want to remove from the set. If the element is present in the set, it will be removed. However, if the element is not found, the remove() method will raise a KeyError exception.

Example
In the following example, we are deleting the element "Physics" from the set "my_set" using the remove() method −
"""
my_set = {"Davoud", "AI", 21, 69.75}
print ("Original set: ", my_set)

my_set.remove("AI")
print ("Set after removing: ", my_set)
"""
It will produce the following output −

Original set:  {21, 69.75, 'Rohan', 'Physics'}
Set after removing:  {21, 69.75, 'Rohan'}
"""
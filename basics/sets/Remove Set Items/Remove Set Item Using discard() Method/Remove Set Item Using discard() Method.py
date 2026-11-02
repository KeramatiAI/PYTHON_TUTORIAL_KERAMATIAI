"""
The discard() method in set class is similar to remove() method. The only difference is, it doesn't raise error even if the object to be removed is not already present in the set collection.

Example
In this example, we are using the discard() method to delete an element from a set regardless of whether it is present or not −
"""
my_set = {"Rohan", "Physics", 21, 69.75}
print ("Original set: ", my_set)

# removing an existing element
my_set.discard("Physics")
print ("Set after removing Physics: ", my_set)

# removing non-existing element
my_set.discard("PHP")
print ("Set after removing non-existent element PHP: ", my_set)
"""
Following is the output of the above code −

Original set:  {21, 'Rohan', 69.75, 'Physics'}
Set after removing Physics:  {21, 'Rohan', 69.75}
Set after removing non-existent element PHP:  {21, 'Rohan', 69.75}
"""
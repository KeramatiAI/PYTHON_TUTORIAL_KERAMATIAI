"""
you can use the discard() function to remove an element from the set if it is present. Unlike remove(), discard() does not raise an error if the element is not found in the set −
"""
my_set = {1, 2, 3, 4}
# No error even if 5 is not in the set
my_set.discard(5)  
print (my_set)
"""
We get the output as shown below −

{1, 2, 3, 4}
"""

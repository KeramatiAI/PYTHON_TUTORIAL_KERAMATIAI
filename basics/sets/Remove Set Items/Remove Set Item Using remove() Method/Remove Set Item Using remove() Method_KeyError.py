"""
Example
If the element to delete is not found in the set, the remove() method will raise a KeyError exception −
"""
my_set = {"Rohan", "Physics", 21, 69.75}
print ("Original set: ", my_set)

my_set.remove("PHP")
print ("Set after removing: ", my_set)
"""
We get the error as shown below −

Original set:  {'Physics', 21, 69.75, 'Rohan'}
Traceback (most recent call last):
  File "/home/cg/root/664c365ac1c3c/main.py", line 4, in <module>
    my_set.remove("PHP")
KeyError: 'PHP'
"""
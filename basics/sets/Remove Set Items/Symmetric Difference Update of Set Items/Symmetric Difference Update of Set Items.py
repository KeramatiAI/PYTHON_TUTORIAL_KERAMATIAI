"""
The symmetric difference between two sets is the collection of all the uncommon items, rejecting the common elements. The symmetric_difference_update() method updates a set with symmetric difference between itself and the set given as argument.

Example
In the example below, we are defining two sets "s1" and "s2", then using the symmetric_difference_update() method to modify "s1" so that it contains elements that are in either "s1" or "s2", but not in both −
"""
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s1.symmetric_difference_update(s2)
print ("s1 after running symmetric difference ", s1)
"""
The result obtained is as shown below −

s1: {1, 2, 3, 4, 5} s2: {4, 5, 6, 7, 8}
s1 after running symmetric difference {1, 2, 3, 6, 7, 8}
"""
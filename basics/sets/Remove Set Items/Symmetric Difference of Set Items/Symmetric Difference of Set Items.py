"""
The symmetric_difference() method in set class is similar to symmetric_difference_update() method, except that it returns a new set object that holds all the items from two sets minus the common items.

Example
In the following example, we are defining two sets "s1" and "s2". We are then using the symmetric_difference() method to create a new set "s3" containing elements that are in either "s1" or "s2", but not in both −
"""
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s3 = s1.symmetric_difference(s2)
print ("s1 = s1^s2 ", s3)
"""
It will produce the following output −

s1: {1, 2, 3, 4, 5} s2: {4, 5, 6, 7, 8}
s1 = s1^s2 {1, 2, 3, 6, 7, 8}
"""
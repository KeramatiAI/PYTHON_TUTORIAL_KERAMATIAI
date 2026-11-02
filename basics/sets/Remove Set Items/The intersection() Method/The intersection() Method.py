"""
The intersection() method in set class is similar to its intersection_update() method, except that it returns a new set object that consists of items common to existing sets.

Syntax
Following is the basic syntax of the intersection() method −

set.intersection(obj)

Where, obj is a set object.

Return value
The intersection() method returns a set object, retaining only those items common in itself and obj.

Example
In the following example, we are defining two sets "s1" and "s2", then using the intersection() method to create a new set "s3" containing elements that are common to both "s1" and "s2" −

"""
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s3 = s1.intersection(s2)
print ("s3 = s1 & s2: ", s3)
"""
It will produce the following output −

s1: {1, 2, 3, 4, 5} s2: {4, 5, 6, 7, 8}
s3 = s1 & s2: {4, 5}
"""

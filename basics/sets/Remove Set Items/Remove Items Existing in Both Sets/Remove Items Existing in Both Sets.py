"""
You can remove items that exist in both sets (i.e., the intersection of two sets) using the difference_update() method or the subtraction operator (-=). This removes all elements that are present in both sets from the original set.

Example
In this example, we are defining two sets "s1" and "s2", and then using the difference_update() method to remove elements from "s1" that are also in "s2" −
"""
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1 before running difference_update: ", s1)
s1.difference_update(s2)
print ("s1 after running difference_update: ", s1)
"""
After executing the above code, we get the following output −

s1 before running difference_update: {1, 2, 3, 4, 5}
s1 after running difference_update: {1, 2, 3}
set()
"""
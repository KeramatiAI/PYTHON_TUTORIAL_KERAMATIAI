"""
You can remove uncommon items between two sets using the intersection_update() method. The intersection of two sets results in a set containing only the elements that are present in both sets.

To keep only the common elements in one of the original sets and remove the uncommon ones, you can update the set with its intersection.

Example
In this example, we are defining two sets "set1" and "set2". We are then using the intersection_update() method to modify "set1" so that it only contains elements that are also in "set2" −
"""
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Keeping only common items in set1
set1.intersection_update(set2)
print("Set 1 after keeping only common items:", set1)
"""
Output of the above code is as shown below −

Set 1 after keeping only common items: {3, 4}
"""
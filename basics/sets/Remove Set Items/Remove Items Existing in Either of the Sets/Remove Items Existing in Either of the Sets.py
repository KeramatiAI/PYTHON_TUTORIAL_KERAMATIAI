"""
To remove items that exist in either of two sets, you can use the symmetric difference operation. The symmetric difference between two sets results in a set containing elements that are in either of the sets but not in their intersection.

In Python, the symmetric difference operation can be performed using the ^ operator or symmetric_difference() method.

Example
In the following example, we are defining two sets "set1" and "set2". We are then using the symmetric difference operator (^) to create a new set "result_set" containing elements that are in either "set1" or "set2" but not in both −
"""
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Removing items that exist in either set
result_set = set1 ^ set2
print("Resulting Set:", result_set)
"""
Following is the output of the above code −

Resulting Set: {1, 2, 5, 6}
"""
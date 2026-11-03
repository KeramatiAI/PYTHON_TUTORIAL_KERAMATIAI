"""
Python Set Union Operator (|)
The union of two sets is a set containing all distinct elements that are in A or in B or both. For example,

{1,2}{2,3}={1,2,3}
The following diagram illustrates the union of two sets.

Union Of Two Sets
In Python, you can perform the union operation using the union() function or the | operator. This operation combines the elements of two sets while eliminating duplicates, resulting in a new set containing all unique elements from both sets −

Example
The following example uses the "|" operator and union() function, and returns the union of two sets −
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 8, 9}
set4 = {9, 45, 73}
union_set1 = set1.union(set2)
union_set2 = set3 | set4
print ('The union of set1 and set2 is', union_set1)
print ('The union of set3 and set4 is', union_set2)
"""
After executing the above code, we get the following output −

The union of set1 and set2 is {1, 2, 3, 4, 5}
The union of set3 and set4 is {73, 6, 8, 9, 45}
"""
"""
Python Set Intersection Operator (&)
The intersection of two sets AA and BB, denoted by A∩B, consists of all elements that are common to both in A and B. For example,

{1,2}∩{2,3}={2}
The following diagram illustrates intersection of two sets.

Intersection Operator
Python provides the intersection() function or the & operator to perform this operation. The resulting set contains only the elements present in both sets −

Example
Following example uses & operator and intersection() function, and returns intersection of two sets −
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 8, 9}
set4 = {9, 8, 73}
intersection_set1 = set1.intersection(set2)
intersection_set2 = set3  & set4
print ('The intersection of set1 and set2 is', intersection_set1)
print ('The intersection of set3 and set4 is', intersection_set2)
"""
It will produce the following output −

The intersection of set1 and set2 is {3}
The intersection of set3 and set4 is {8, 9}
"""
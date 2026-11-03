"""
Python Set Difference Operator (-)
The difference (subtraction) between two sets consists of elements present in the first set but not in the second set. It is defined as follows. The set AB consists of elements that are in A but not in B. For example,

If A={1,2,3} and B={3,5}, then AB={1,2}
The following diagram illustrates difference of two sets −

difference_operator
Python provides the difference() function or the - operator to perform this operation. The resulting set contains elements unique to the first set −

Example
The following example uses the "-" operator and the difference() function, and returns difference of two sets −
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 8, 9}
set4 = {9, 8, 73}
difference_set1 = set1.difference(set2)
difference_set2 = set3 - set4
print ('The difference between set1 and set2 is', difference_set1)
print ('The difference between set3 and set4 is', difference_set2)
"""
We get the output as shown below −

The difference between set1 and set2 is {1, 2}
The difference between set3 and set4 is {6}
Note that "s1-s2" is not the same as "s2-s1".
"""
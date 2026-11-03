"""
Python Set Symmetric Difference Operator
The symmetric difference of two sets consists of elements that are present in either set but not in both sets. The symmetric difference of A and B is denoted by "A Δ B" and is defined by −

A Δ B = (A − B) &Union; (B − A)
If A = {1, 2, 3, 4, 5, 6, 7, 8} and B = {1, 3, 5, 6, 7, 8, 9}, then A Δ B = {2, 4, 9}.

The following diagram illustrates the symmetric difference between two sets −

Symmetric Difference
Python provides the symmetric_difference() function or the ^ operator to perform this operation. The resulting set contains elements that are unique to each set.

Example
The following example uses the "^" operator and the symmetric_difference() function, and returns symbolic difference of two sets −
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 8, 9}
set4 = {9, 8, 73}
symmetric_difference_set1 = set1.symmetric_difference(set2)
symmetric_difference_set2 = set3 ^ set4
print ('The symmetric difference of set1 and set2 is', symmetric_difference_set1)
print ('The symmetric difference of set3 and set4 is', symmetric_difference_set2)
"""
The result produced is as follows −

The symmetric difference of set1 and set2 is {1, 2, 4, 5}
The symmetric difference of set3 and set4 is {73, 6}
"""
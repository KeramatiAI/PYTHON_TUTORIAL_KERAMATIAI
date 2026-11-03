"""
Python Subset Testing Operation
You can check whether one set is a subset of another using the issubset() function or the <= operator. A set A is considered a subset of another set B if all elements of A are also present in B −

Example
The following example uses the "<=" operator and the issubset() function, and returns subset testing of two sets −
"""
set1 = {1, 2}
set2 = {1, 2, 3, 4}
set3 = {64, 47, 245, 48}
set4 = {64, 47, 3}
is_subset1 = set1.issubset(set2)
is_subset2 = set3 <= set4
print ('set1 is a subset of set2:', is_subset1)
print ('set3 is a subset of set4:', is_subset2)
"""
The result produced is as follows −

set1 is a subset of set2: True
set3 is a subset of set4: False
"""
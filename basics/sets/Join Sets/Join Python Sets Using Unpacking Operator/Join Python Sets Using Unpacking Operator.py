"""
In Python, the "*" symbol is used as unpacking operator. The unpacking operator internally assign each element in a collection to a separate variable.

We can join Python sets using the unpacking operator (*) by unpacking the elements of multiple sets into a new set.

Example
In the following example, we are creating a new set "s3" by unpacking the elements of sets "s1" and "s2" using the * operator within a set literal −
"""
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = {*s1, *s2}
print (s3)
"""
The output produced is as follows −

{1, 2, 3, 4, 5, 6, 7, 8}
"""
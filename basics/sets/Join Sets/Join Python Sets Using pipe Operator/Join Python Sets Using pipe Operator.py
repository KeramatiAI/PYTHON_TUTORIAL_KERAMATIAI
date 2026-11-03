"""
The "|" symbol (pipe) is defined as the union operator. It performs the A ∪ B operation and returns a set of items in A, B or both. Set doesn't allow duplicate items.

Example
In the following example, we are performing a union operation on sets "s1" and "s2" using the "|" operator, creating a new set "s3" containing elements from both sets without duplicates −
"""
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = s1|s2
print (s3)
"""
It will produce the following output −

{1, 2, 3, 4, 5, 6, 7, 8}
"""
"""
The set class has union() method that performs the same operation as | operator. It returns a set object that holds all items in both sets, discarding duplicates.

Example
In this example, we are invoking the union() method on set "s1", passing set "s2" as an argument, which returns a new set "s3" containing elements from both sets without duplicates −
"""
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = s1.union(s2)
print (s3)
"""
Following is the output obtained −

{1, 2, 3, 4, 5, 6, 7, 8}
"""
"""
The update() method also joins the two sets, as the union() method. However it doesn't return a new set object. Instead, the elements of second set are added in first, duplicates not allowed.

Example
In the example below, we are updating set "s1" with the elements of set "s2" using the update() method, modifying "s1" to contain elements from both sets without duplicates −
"""
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.update(s2)
print (s1)
"""
The result obtained is as shown below −

{1, 2, 3, 4, 5, 6, 7, 8}
"""
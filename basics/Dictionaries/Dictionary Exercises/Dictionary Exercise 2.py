"""
Python program to convert a dictionary to list of (k,v) tuples.
"""
d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
L1 = list(d1.items())
print (L1)
"""
It will produce the following output −

[('one', 11), ('two', 22), ('three', 33), ('four', 44), ('five', 55)]
"""
"""
Python program to create a new dictionary by extracting the keys from a given dictionary.
"""
d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
keys = ['two', 'five']
d2={}
for k in keys:
   d2[k]=d1[k]
print (d2)
"""
It will produce the following output −

{'two': 22, 'five': 55}
"""
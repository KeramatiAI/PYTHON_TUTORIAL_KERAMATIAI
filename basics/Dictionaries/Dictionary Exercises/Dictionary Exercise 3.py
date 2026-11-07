"""
Python program to remove keys with same values in a dictionary.
"""
d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
vals = list(d1.values())#all values
uvals = [v for v in vals if vals.count(v)==1]#unique values
d2 = {}
for k,v in d1.items():
   if v in uvals:
      d = {k:v}
      d2.update(d)
print ("dict with unique value:",d2)
"""
It will produce the following output −

dict with unique value: {'three': 3, 'four': 44}
"""
"""
Dictionary Exercise Programs
Python program to sort list of dictionaries by values

Python program to extract dictionary with each key having non-numeric value from a given dictionary.

Python program to build a dictionary from list of two item (k,v) tuples.

Python program to merge two dictionary objects, using unpack operator.
"""
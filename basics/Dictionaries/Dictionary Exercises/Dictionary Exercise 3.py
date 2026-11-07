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
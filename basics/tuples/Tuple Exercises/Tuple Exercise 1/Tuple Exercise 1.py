"""
Python program to find unique numbers in a given tuple −
"""
T1 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
T2 = ()
for x in T1:
   if x not in T2:
      T2+=(x,)
print ("original tuple:", T1)
print ("Unique numbers:", T2)
"""
It will produce the following output −

original tuple: (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
Unique numbers: (1, 9, 6, 3, 4, 5, 2, 7, 8)
"""
"""
Python program to create a tuple of 5 random integers −
"""
import random
t1 = ()
for i in range(5):
   x = random.randint(0, 100)
   t1+=(x,)
print (t1)
"""
It will produce the following output −

(64, 21, 68, 6, 12)

"""
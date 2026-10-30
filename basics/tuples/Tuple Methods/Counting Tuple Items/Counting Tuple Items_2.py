"""
Even if the items in the tuple contain expressions, they will be evaluated to obtain the count.
"""
tup1 = (10, 20/80, 0.25, 10/40, 30, 10, 55)
print ("Tup1:", tup1)
c = tup1.count(0.25)
print ("count of 10:", c)
"""
It will produce the following output −

Tup1: (10, 0.25, 0.25, 0.25, 30, 10, 55)
count of 10: 3
"""
"""
Python program to find sum of all numbers in a tuple −
"""
T1 = (1, 9, 1, 6, 3, 4)
ttl = 0
for x in T1:
   ttl+=x

print ("Sum of all numbers Using loop:", ttl)

ttl = sum(T1)
print ("Sum of all numbers sum() function:", ttl)
"""
It will produce the following output −

Sum of all numbers Using loop: 24
Sum of all numbers sum() function: 24
"""
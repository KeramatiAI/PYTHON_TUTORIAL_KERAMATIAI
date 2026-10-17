"""
Syntax
The range() function has the following syntax −

range(start, stop, step)

Start − Starting value of the range. Optional. Default is 0

Stop − The range goes upto stop-1

Step − Integers in the range increment by the step value. Option, default is 1.
"""
for num in range(5):
   print (num, end=' ')
print()
for num in range(10, 20):
   print (num, end=' ')
print()
for num in range(1, 10, 2):
   print (num, end=' ')

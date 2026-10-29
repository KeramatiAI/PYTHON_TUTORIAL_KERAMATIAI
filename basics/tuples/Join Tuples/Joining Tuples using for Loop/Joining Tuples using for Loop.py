"""
A for loop in Python is used for iterating over a sequence (such as a list, tuple, string, or range) and executing a block of code for each element in the sequence. The loop continues until all elements have been processed.

We can join a tuple using a for loop by iterating over the elements of one tuple and appending each element to another tuple with the "+=" operator.

Example
In the following example, we are iterating over each element in tuple T2, and for each element, we are appending it to tuple T1, effectively joining the two tuples −
"""
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
for t in T2:
   T1+=(t,)
print (T1)
"""
A for loop in Python is a control flow statement used for iterating over a sequence and executing a block of code for each element in the sequence. The loop continues until all elements have been processed.

We can access set items using a for loop by iterating over each element in the set sequentially. Since sets are unordered collections of unique elements, a for loop provides a convenient way to traverse the set and access each element one by one.

Example
In the following example, the for loop iterates over the set "langs", and in each iteration, the variable "lang" is assigned the value of the current element −
"""
# Defining a set
langs = {"C", "C++", "Java", "Python"}

# Accessing set items using a for loop
for lang in langs:
   print (lang)
"""
It will produce the following output −

Python
C
C++
Java
"""
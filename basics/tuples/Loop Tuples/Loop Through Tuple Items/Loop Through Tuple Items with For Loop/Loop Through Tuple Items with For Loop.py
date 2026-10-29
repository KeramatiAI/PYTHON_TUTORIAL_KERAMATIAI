"""
Loop Through Tuple Items with For Loop
A for loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, string, or range) or any other iterable object. It allows you to execute a block of code repeatedly for each item in the sequence.

In a for loop, you can access each item in a sequence using a variable, allowing you to perform operations or logic based on that item's value. We can loop through tuple items using for loop by iterating over each item in the tuple.

Syntax
Following is the basic syntax to loop through items in a tuple using a for loop in Python −

for item in tuple:
   # Code block to execute

"""
tup = (25, 12, 10, -21, 10, 100)
for num in tup:
   print (num, end = ' ')
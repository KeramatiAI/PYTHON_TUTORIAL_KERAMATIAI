"""
Loop Through Dictionary Using a For Loop
A for loop in Python is a control flow statement that iterates over a sequence of elements. It repeatedly executes a block of code for each item in the sequence. The sequence can be a range of numbers, a list, a tuple, a string, or any iterable object.

We can loop through dictionaries using a for loop in Python by iterating over the keys or key-value pairs within the dictionary. There are two common approaches −

Example: Iterating over Keys
In this approach, the loop iterates over the keys of the dictionary. Inside the loop, you can access the value corresponding to each key using dictionary indexing −
"""
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
for key in student:
   print(key, student[key])
"""
It will produce the following output −

name Alice
age 21
major Computer Science
"""
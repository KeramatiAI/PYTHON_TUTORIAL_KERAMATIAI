"""
A for loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, string, or range) or any other iterable object. It allows you to execute a block of code repeatedly for each item in the sequence.

In a for loop, you can access each item in a sequence using a variable, allowing you to perform operations or logic based on that item's value. We can loop through set items using for loop by iterating over each item in the set.

Syntax
Following is the basic syntax to loop through items in a set using a for loop in Python −

for item in set:
   # Code block to execute
Example
In the following example, we are using a for loop to iterate through each element in the set "my_set" and retrieving each element −
"""
# Defining a set with multiple elements
my_set = {25, 12, 10, -21, 10, 100}

# Loop through each item in the set
for item in my_set:
   # Performing operations on each element
   print("Item:", item)
"""
Output

Following is the output of the above code −

Item: 100
Item: 25
Item: 10
Item: -21
Item: 12
"""
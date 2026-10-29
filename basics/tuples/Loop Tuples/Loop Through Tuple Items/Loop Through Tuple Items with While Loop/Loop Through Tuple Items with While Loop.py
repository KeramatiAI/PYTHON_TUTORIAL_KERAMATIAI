"""
Loop Through Tuple Items with While Loop
A while loop in Python is used to repeatedly execute a block of code as long as a specified condition evaluates to "True".

We can loop through tuple items using while loop by initializing an index variable, then iterating through the tuple using the index variable and incrementing it until reaching the end of the tuple.

An index variable is used within a loop to keep track of the current position or index in a sequence, such as a tuple or array. It is generally initialized before the loop and updated within the loop to iterate over the sequence.
Syntax
Following is the basic syntax for looping through items in a tuple using a while loop in Python −

while condition:
   # Code block to execute

"""
my_tup = (1, 2, 3, 4, 5)
index = 0

while index < len(my_tup):
   print(my_tup[index])
   index += 1
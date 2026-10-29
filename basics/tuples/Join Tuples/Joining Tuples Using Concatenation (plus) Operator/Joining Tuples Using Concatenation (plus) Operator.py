"""
The concatenation operator in Python, denoted by +, is used to join two sequences, such as strings, lists, or tuples, into a single sequence. When applied to tuples, the concatenation operator joins the elements of the two (or more) tuples to create a new tuple containing all the elements from both tuples.

We can join tuples using the concatenation operator by simply using the + symbol to concatenate them.

Example
In the following example, we are concatenating the elements of two tuples "T1" and "T2", creating a new tuple "joined_tuple" containing all the elements from both tuples −
"""
# Two tuples to be joined
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
# Joining the tuples
joined_tuple = T1 + T2

# Printing the joined tuple
print("Joined Tuple:", joined_tuple)
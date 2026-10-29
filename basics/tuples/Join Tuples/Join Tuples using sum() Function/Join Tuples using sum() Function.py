"""
In Python, the sum() function is used to add up all the elements in an iterable, such as a list, tuple, or set. It takes an iterable as its argument and returns the sum of all the elements in that iterable.

We can join a tuple using the sum() function by providing the tuple as an argument to the sum() function. However, since the sum() function is specifically designed for numeric data types, this method only works for tuples containing numeric elements. It will add up all the numeric elements in the tuple and return their sum.

Syntax
Following is the syntax for using the sum() function to join tuples in Python −

result_tuple = sum((tuple1, tuple2), ())
Here, the first argument is a tuple containing the tuples to be joined. The second argument is the starting value for the sum. Since we are joining tuples, we use an empty tuple () as the starting value.
"""
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T3 = sum((T1, T2), ())
print ("Joined Tuple:", T3)
tuple_1 = ('physics', 'chemistry', 1997, 2000)
print (tuple_1)
del tuple_1
print ("After deleting tuple : ")
print (tuple_1) # NameError: name 'tuple_1' is not defined.
"""
Python Tuple Operations
In Python, Tuple is a sequence. Hence, we can concatenate two tuples with + operator and concatenate multiple copies of a tuple with "*" operator. The membership operators "in" and "not in" work with tuple object.

Python Expression	Results	Description
(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	Concatenation
('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	Repetition
3 in (1, 2, 3)	True	Membership
"""
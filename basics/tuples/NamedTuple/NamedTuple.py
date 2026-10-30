"""
In Python, tuples are immutable data structures that can hold a collection of items. We already discussed tuples, it's properties and usage in the previous chapters. In this chapter, we will explain namedtuple() and its usage in Python.

What is NamedTuple?
In Python, a namedtuple() is a subclass of tuple that allows you to create tuples with named fields. Meaning, you can access the elements of the tuple using fieldnames instead of just numerical indices. It is part of the collections module in Python.

Syntax
from collections import namedtuple

# Define a namedtuple
Point = namedtuple('typename', fieldnames )
Type Name: The typename is the name of the namedtuple class. It is a string that represents the name of the tuple type.
Field Names: The field names are the names of the elements in the tuple. They are defined as a list of strings.

"""
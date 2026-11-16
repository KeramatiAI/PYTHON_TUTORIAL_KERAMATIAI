"""
The dataclass is a feature in Python that helps for automatically adding special methods to user-defined classes. For example, a dataclass can be used to automatically generate a constructor method for your class, so you can easily create instances of the class. In this chapter, we will explain all the features of the dataclass module with the help of examples.

What is a Dataclass?
A dataclass is a Python class denoted with the @dataclass decorator from the dataclasses module. It is used to automatically generate special methods like constructor method __init__(), string representation method __repr__(), equality method __eq__(), and others based on the class attributes defined in the class body. This simply means that using dataclasses can reduce boilerplate code in your class definitions.

Syntax of Dataclass
The syntax to define a dataclass is as follows −

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
Each argument is taking a boolean value, which indicates whether corresponding special methods should be automatically generated.

The @dataclass decorator can take these options:

init (default: True) − Automatically creates an __init__() method for initializing class instances.
repr (default: True) − Automatically creates a __repr__() method to provide a readable string representation of the object.
eq (default: True) − Generates an __eq__() method for comparing objects using the == operator.
order (default: False) − If set to True, comparison methods (like < and >) are generated for sorting objects.
unsafe_hash (default: False) − If false, it produces a default __hash__() method based on how equality and mutability are defined.
frozen (default: False) − Creates immutable instances (they can’t be changed after creation).
"""
"""
Enums in Python
In Python, the term enumeration refers to the process of assigning fixed constant values to a set of strings so that each string can be identified by the value bound to it. The Enum class included in enum module (which is a part of Python's standard library) is used as the parent class to define enumeration of a set of identifiers − conventionally written in upper case.

Example
In the below code, "subjects" is the enumeration. It has different enumeration members and each member is an object of the enumeration class subjects. These members have name and value attributes.
"""
# importing enum
from enum import Enum

class subjects(Enum):
   ENGLISH = 1
   MATHS = 2
   SCIENCE = 3
   SANSKRIT = 4

obj = subjects.MATHS
print (type(obj))
"""
It results in following output −

<enum 'subjects'> 
An enum class cannot have the same member appearing twice, however, more than one member may be assigned the same value. To ensure that each member has a unique value bound to it, use the @unique decorator.
"""
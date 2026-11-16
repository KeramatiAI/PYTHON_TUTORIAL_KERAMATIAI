"""
Example
In this example, we are using the @unique decorator to restrict duplicacy.
"""
from enum import Enum, unique

@unique
class subjects(Enum):
   ENGLISH = 1
   MATHS = 2
   GEOGRAPHY = 3
   SANSKRIT = 2
"""
This will raise an exception as shown below −

   @unique
    ^^^^^^
   raise ValueError('duplicate values found in %r: %s' %
ValueError: duplicate values found in <enum 'subjects'>: SANSKRIT -> MATHS
The Enum class is a callable class, hence you can use its constructor to create an enumeration. This constructor accepts two arguments, which are the name of enumeration and a string consisting of enumeration member symbolic names separated by a whitespace.


"""
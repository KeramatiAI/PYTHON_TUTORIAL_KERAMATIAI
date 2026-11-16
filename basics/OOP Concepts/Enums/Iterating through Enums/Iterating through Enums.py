"""
Iterating through Enums
You can iterate through the enum members in the order of their appearance in the definition, with the help of a for loop.

Example
The following example shows how to iterate through an enumeration using for loop −
"""
from enum import Enum

class subjects(Enum):
   ENGLISH = "E"
   MATHS = "M"
   GEOGRAPHY = "G"
   SANSKRIT = "S"

for sub in subjects:
   print (sub.name, sub.value)
"""
It will produce the following output −

ENGLISH E
MATHS M
GEOGRAPHY G
SANSKRIT S
We know that enum member can be accessed with the unique value assigned to it, or by its name attribute. Hence, subjects("E") as well as subjects["ENGLISH"] returns subjects.ENGLISH member.
"""
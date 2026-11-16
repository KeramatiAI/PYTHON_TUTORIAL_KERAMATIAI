"""
Accessing Modes in Enums
Members of an enum class can be accessed in two modes −

Value − In this mode, value of the enum member is accessed using the "value" keyword followed by object of the enum class.

Name − Similarly, we use the "name" keyword to access name of the enum member.

Example
The following example illustrates how to access value and name of the enum member.
"""
from enum import Enum

class subjects(Enum):
   ENGLISH = "E"
   MATHS = "M"
   GEOGRAPHY = "G"
   SANSKRIT = "S"

obj = subjects.SANSKRIT
print(type(obj))
print(obj.name)
print(obj.value)
"""
It will produce the following output −

<enum 'subjects'> 
SANSKRIT
S
"""
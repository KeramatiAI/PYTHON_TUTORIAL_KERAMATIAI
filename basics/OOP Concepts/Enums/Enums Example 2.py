"""
Example
following is an alternative method of defining an enumeration −
"""
from enum import Enum
subjects = Enum("subjects", "ENGLISH MATHS SCIENCE SANSKRIT")
print(subjects.ENGLISH)
print(subjects.MATHS)
print(subjects.SCIENCE)
print(subjects.SANSKRIT)
"""
This code will give the following output −

subjects.ENGLISH
subjects.MATHS
subjects.SCIENCE
subjects.SANSKRIT
"""
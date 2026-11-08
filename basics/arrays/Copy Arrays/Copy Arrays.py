"""
In Python, copying an array refers to the process of creating a new array that contains all the elements of the original array. This operation can be done using assignment operator (=) and deepcopy() method. In this chapter, we discuss how to copy an array object to another. But, before getting into the details let's breifly discuss arrays.

Python's built-in sequence types i.e. list, tuple, and string are indexed collection of items. However, unlike arrays in C/C++, Java etc. they are not homogenous, in the sense the elements in these types of collection may be of different types. Python's array module helps you to create object similar to Java like arrays.

Python arrays can be of string, integer or float type. The array class constructor is used as follows −

import array
obj = array.array(typecode[, initializer])
Where, the typecode may be a character constant representing the data type.
"""
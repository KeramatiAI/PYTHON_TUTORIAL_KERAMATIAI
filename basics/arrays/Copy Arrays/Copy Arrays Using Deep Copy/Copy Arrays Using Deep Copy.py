"""
Copy Arrays Using Deep Copy
To create another physical copy of an array, we use another module in Python library, named copy and use deepcopy() function in the module. A deep copy constructs a new compound object and then, recursively inserts copies into it of the objects found in the original.

Example
The following example demonstrates how to copy array in Python −
"""
import array as arr
import copy
a = arr.array('i', [110, 220, 330, 440, 550])
b = copy.deepcopy(a)
print("Copied array:",b)
"""
On executing, it will produce the following output −

Copied array: array('i', [110, 220, 330, 440, 550])
Now check the id() of both "a" and "b". You will find the ids are different.

print (id(a), id(b))
It will produce the following output −

2771967069936 2771967068976
This proves that a new object "b" is created which is an actual copy of "a". If we change an element in "a", it is not reflected in "b".

a[2]=10
print (a,b)
It will produce the following output −

array('i', [110, 220, 10, 440, 550]) array('i', [110, 220, 330, 440, 550])
"""
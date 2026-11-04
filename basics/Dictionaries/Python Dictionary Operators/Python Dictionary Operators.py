"""
Python Dictionary Operators
In Python, following operators are defined to be used with dictionary operands. In the example, the following dictionary objects are used.
"""
d1 = {'a': 2, 'b': 4, 'c': 30}
d2 = {'a1': 20, 'b1': 40, 'c1': 60}
"""
Operator	Description	Example
dict[key]	Extract/assign the value mapped with key	print (d1['b']) retrieves 4
d1['b'] = 'Z' assigns new value to key 'b'

dict1|dict2	Union of two dictionary objects, returning new object (Python 3.9+)	d3=d1|d2 ; print (d3)
{'a': 2, 'b': 4, 'c': 30, 'a1': 20, 'b1': 40, 'c1': 60}

dict1|=dict2	Augmented dictionary union operator (Python 3.9+)	d1|=d2; print (d1)
{'a': 2, 'b': 4, 'c': 30, 'a1': 20, 'b1': 40, 'c1': 60}
"""
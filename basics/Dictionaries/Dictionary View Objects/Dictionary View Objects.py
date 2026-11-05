"""
The items(), keys(), and values() methods of dict class return view objects. These views are refreshed dynamically whenever any change occurs in the contents of their source dictionary object.

The items() Method
The items() method returns a dict_items view object. It contains a list of tuples, each tuple made up of respective key, value pairs.

Syntax
Following is the syntax of the items() method −

Obj = dict.items()
Return value
The items() method returns dict_items object which is a dynamic view of (key,value) tuples.

Example
In the following example, we first obtain the dict_items object with items() method and check how it is dynamically updated when the dictionary object is updated.
"""
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.items()
print ('type of obj: ', type(obj))
print (obj)
print ("update numbers dictionary")
numbers.update({50:"Fifty"})
print ("View automatically updated")
print (obj)
"""
It will produce the following output −

type of obj: <class 'dict_items'>
dict_items([(10, 'Ten'), (20, 'Twenty'), (30, 'Thirty'), (40, 'Forty')])
update numbers dictionary
View automatically updated
dict_items([(10, 'Ten'), (20, 'Twenty'), (30, 'Thirty'), (40, 'Forty'), (50, 'Fifty')])
"""
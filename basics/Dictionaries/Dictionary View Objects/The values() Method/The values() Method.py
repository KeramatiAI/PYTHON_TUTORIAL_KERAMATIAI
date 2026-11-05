"""
The values() Method
The values() method returns a view of all the values present in the dictionary. The object is of dict_value type, which gets automatically updated.

Syntax
Following is the syntax of the values() method −

Obj = dict.values()
Return value
The values() method returns a dict_values view of all the values present in the dictionary.

Example
In the example below, we obtain a view object "obj" of the values using the values() method from the "numbers" dictionary −
"""
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.values()
print ('type of obj: ', type(obj))
print (obj)
print ("update numbers dictionary")
numbers.update({50:"Fifty"})
print ("View automatically updated")
print (obj)
"""
It will produce the following output −

type of obj: <class 'dict_values'>
dict_values(['Ten', 'Twenty', 'Thirty', 'Forty'])
update numbers dictionary
View automatically updated
dict_values(['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty'])
"""
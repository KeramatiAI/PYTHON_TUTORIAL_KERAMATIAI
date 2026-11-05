"""
The keys() Method
The keys() method of dict class returns dict_keys object which is a list of all keys defined in the dictionary. It is a view object, as it gets automatically updated whenever any update action is done on the dictionary object.

Syntax
Following is the syntax of the keys() method −

Obj = dict.keys()
Return value
The keys() method returns dict_keys object which is a view of keys in the dictionary.

Example
In this example, we are creating a dictionary named "numbers" with integer keys and their corresponding string values. Then, we obtain a view object "obj" of the keys using the keys() method, and retrieve its type and content −
"""
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.keys()
print ('type of obj: ', type(obj))
print (obj)
print ("update numbers dictionary")
numbers.update({50:"Fifty"})
print ("View automatically updated")
print (obj)
"""
It will produce the following output −

type of obj: <class 'dict_keys'>
dict_keys([10, 20, 30, 40])
update numbers dictionary
View automatically updated
dict_keys([10, 20, 30, 40, 50])
"""
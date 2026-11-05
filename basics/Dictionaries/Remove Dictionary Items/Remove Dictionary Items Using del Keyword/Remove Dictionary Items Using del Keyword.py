"""
Remove Dictionary Items Using del Keyword
The del keyword in Python is used to delete objects. In the context of dictionaries, it is used to remove an item or a slice of items from the dictionary, based on the specified key(s).

We can remove dictionary items using the del keyword by specifying the key of the item we want to remove. This will delete the key-value pair associated with the specified key from the dictionary.

Example 1
In the following example, we are creating a dictionary named numbers with integer keys and their corresponding string values. Then, delete the item with the key '20' using the del keyword −
"""
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before delete operation: \n", numbers)
del numbers[20]
print ("numbers dictionary before delete operation: \n", numbers)
"""
It will produce the following output −

numbers dictionary before delete operation: 
 {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
numbers dictionary before delete operation: 
 {10: 'Ten', 30: 'Thirty', 40: 'Forty'}
"""
"""
Remove Dictionary Items Using pop() Method
The pop() method in Python is used to remove a specified key from a dictionary and return the corresponding value. If the specified key is not found, it can optionally return a default value instead of raising a KeyError.

We can remove dictionary items using the pop() method by specifying the key of the item we want to remove. This method will return the value associated with the specified key and remove the key-value pair from the dictionary.

Example
In this example, we are using the pop() method to remove the item with the key '20' (storing its value in val) from the 'numbers' dictionary. We then retrieve the updated dictionary and the popped value −
"""
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before pop operation: \n", numbers)
val = numbers.pop(20)
print ("nubvers dictionary after pop operation: \n", numbers)
print ("Value popped: ", val)
"""
Following is the output of the above code −

numbers dictionary before pop operation: 
 {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
nubvers dictionary after pop operation: 
 {10: 'Ten', 30: 'Thirty', 40: 'Forty'}
Value popped:  Twenty
"""
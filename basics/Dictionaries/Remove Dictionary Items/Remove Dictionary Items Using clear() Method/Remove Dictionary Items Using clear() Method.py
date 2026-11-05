"""
Remove Dictionary Items Using clear() Method
The clear() method in Python is used to remove all items from a dictionary. It effectively empties the dictionary, leaving it with a length of 0.

We can remove dictionary items using the clear() method by calling it on the dictionary object. This method removes all key-value pairs from the dictionary, effectively making it empty.

Example
In the following example, we are using the clear() method to remove all items from the dictionary 'numbers' −
"""
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before clear method: \n", numbers)
numbers.clear()
print ("numbers dictionary after clear method: \n", numbers)
"""
We get the output as shown below −

numbers dictionary before clear method: 
 {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
numbers dictionary after clear method: 
 {}
"""
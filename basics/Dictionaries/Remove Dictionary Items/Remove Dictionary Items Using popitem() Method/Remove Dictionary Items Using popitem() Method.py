"""
Remove Dictionary Items Using popitem() Method
The popitem() method in Python is used to remove and return the last key-value pair from a dictionary.

Since Python 3.7, dictionaries maintain the insertion order, so popitem() removes the most recently added item. If the dictionary is empty, calling popitem() raises a KeyError.
We can remove dictionary items using the popitem() method by calling the method on the dictionary, which removes and returns the last key-value pair added to the dictionary.

Example
In the example below, we use the popitem() method to remove an arbitrary item from the dictionary 'numbers' (storing both its key-value pair in val), and retrieve the updated dictionary along with the popped key-value pair −
"""
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before pop operation: \n", numbers)
val = numbers.popitem()
print ("numbers dictionary after pop operation: \n", numbers)
print ("Value popped: ", val)
"""
Output of the above code is as shown below −

numbers dictionary before pop operation: 
 {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
numbers dictionary after pop operation: 
 {10: 'Ten', 20: 'Twenty', 30: 'Thirty'}
Value popped:  (40, 'Forty')
"""
"""
Example 2
The del keyword, when used with a dictionary object, removes the dictionary from memory −
"""
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before delete operation: \n", numbers)
del numbers
print ("numbers dictionary before delete operation: \n", numbers)
"""
Following is the output obtained −

numbers dictionary before delete operation:
 {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
Traceback (most recent call last):
 File "C:\Users\mlath\examples\main.py", line 5, in <module>
  print ("numbers dictionary before delete operation: \n", numbers)
                                                           ^^^^^^^
NameError: name 'numbers' is not defined
"""
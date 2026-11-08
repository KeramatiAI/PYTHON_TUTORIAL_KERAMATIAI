"""
Example 2
Python program to store all even numbers from an array in another array −
"""
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
b = arr.array('i')
for i in range(len(a)):
   if a[i]%2 == 0:
      b.append(a[i])
print ("Even numbers:", b)
"""
It will produce the following output −

array('i', [10, 5, 15, 4, 6, 20, 9])
Even numbers: array('i', [10, 4, 6, 20])
"""
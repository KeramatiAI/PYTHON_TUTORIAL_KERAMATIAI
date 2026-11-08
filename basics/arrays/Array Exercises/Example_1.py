"""
Example 1
Python program to find the largest number in an array −
"""
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
largest = a[0]
for i in range(1, len(a)):
   if a[i]>largest:
      largest=a[i]
print ("Largest number:", largest)
"""
It will produce the following output −

array('i', [10, 5, 15, 4, 6, 20, 9])
Largest number: 20
"""
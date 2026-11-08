"""
Sort Arrays Using a Sorting Algorithm
We implement the classical bubble sort algorithm to obtain the sorted array. To do it, we use two nested loops and swap the elements for rearranging in sorted order.

Example
Run the following code using a Python code editor −
"""
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
for i in range(0, len(a)):
   for j in range(i+1, len(a)):
      if(a[i] > a[j]):
         temp = a[i];
         a[i] = a[j];
         a[j] = temp;
print (a)
"""
It will produce the following output −

array('i', [4, 5, 6, 9, 10, 15, 20])
"""
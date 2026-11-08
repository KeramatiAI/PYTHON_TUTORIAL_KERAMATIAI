"""
Using indexing
The process of accessing elements of an array through the index is known as Indexing. In this process, we simply need to pass the index number inside the index operator []. The index of an array in Python starts with 0 which means you can find its first element at index 0 and the last at one less than the length of given array.

Example
The following example shows how to access elements of an array using indexing.
"""
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

#indexing
print (numericArray[0])
print (numericArray[1])
print (numericArray[2])
"""
When you run the above code, it will show the following output −

111
211
311
"""
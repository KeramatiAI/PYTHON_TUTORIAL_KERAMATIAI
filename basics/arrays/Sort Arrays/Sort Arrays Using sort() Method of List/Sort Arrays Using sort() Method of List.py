"""
Sort Arrays Using sort() Method of List
Even though array module doesn't have a sort() method, Python's built-in List class does have a sort method. We shall use it in the next example.

First, declare an array and obtain a list object from it, using tolist() method. Then, use the sort() method to get a sorted list. Lastly, create another array using the sorted list which will display a sorted array.

Example
The following code shows how to get sorted array using the sort() method.
"""
import array as arr

# creating array
orgnlArray = arr.array('i', [10,5,15,4,6,20,9])
print("Original array:", orgnlArray)
# converting to list
sortedList = orgnlArray.tolist()
# sorting the list
sortedList.sort()

# creating array from sorted list
sortedArray = arr.array('i', sortedList)
print("Array after sorting:",sortedArray)
"""
The above code will display the following output −

Original array: array('i', [10, 5, 15, 4, 6, 20, 9])
Array after sorting: array('i', [4, 5, 6, 9, 10, 15, 20])
"""
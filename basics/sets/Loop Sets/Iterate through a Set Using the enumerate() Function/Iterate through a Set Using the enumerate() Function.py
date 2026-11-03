"""
The enumerate() function in Python is used to iterate over an iterable object while also providing the index of each element.

We can iterate through a set using the enumerate() function by converting the set into a list and then applying enumerate() to iterate over the elements along with their index positions. Following is the syntax −

for index, item in enumerate(list(my_set)):
   # Your code here
Example
In the following example, we are first converting a set into a list. Then, we iterate through the list using a for loop with enumerate() function, retrieving each item along with its index −
"""
# Converting the set into a list
my_set = {1, 2, 3, 4, 5}
set_list = list(my_set)

# Iterating through the list
for index, item in enumerate(set_list):
   print("Index:", index, "Item:", item)
"""
Output

The output produced is as shown below −

Index: 0 Item: 1
Index: 1 Item: 2
Index: 2 Item: 3
Index: 3 Item: 4
Index: 4 Item: 5
"""
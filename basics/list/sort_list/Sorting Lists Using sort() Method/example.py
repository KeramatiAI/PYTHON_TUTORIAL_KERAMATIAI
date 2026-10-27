"""
Syntax
The syntax for using the sort() method is as follows −

list_name.sort(key=None, reverse=False)
Where,

list_name is the name of the list to be sorted.
key (optional) is a function that defines the sorting criterion. If provided, it is applied to each element of the list for sorting. Default is None.
reverse (optional) is a boolean value. If True, the list will be sorted in descending order. If False (default), the list will be sorted in ascending order.

"""
list1 = ['physics', 'Biology', 'chemistry', 'maths']
print ("list before sort:", list1)
list1.sort()
print ("list after sort : ", list1)
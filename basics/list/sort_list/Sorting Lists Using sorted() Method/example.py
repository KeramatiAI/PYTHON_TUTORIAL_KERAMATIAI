"""
Syntax
The syntax for using the sorted() method is as follows −

sorted(iterable, key=None, reverse=False)
Where,

iterable is the iterable (e.g., list, tuple, string) whose elements are to be sorted.
key (optional) is a function that defines the sorting criterion. If provided, it is applied to each element of the iterable for sorting. Default is None.
reverse (optional) is a boolean value. If True, the iterable will be sorted in descending order. If False (default), the iterable will be sorted in ascending order.

"""
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Sorting in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)
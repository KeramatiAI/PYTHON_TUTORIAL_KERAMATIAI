"""
The append() function is used to add a single element to the end of a list. However, since tuples are immutable, the append() function cannot be directly used to update a tuple.

To update a tuple using the append() function, we need to first convert the tuple to a list, then use append() to add elements, and finally convert the list back to a tuple.

Example
In the following example, we first convert the original tuple "T1" to a list "list_T1". We then use a loop to iterate over the new elements and append each one to the list using the append() function. Finally, we convert the updated list back to a tuple to get the updated tuple −

"""
# Original tuple
T1 = (10, 20, 30, 40)
# Convert tuple to list
list_T1 = list(T1)
# Elements to be added
new_elements = [50, 60, 70]
# Updating the list using append()
for element in new_elements:
    list_T1.append(element)
# Converting list back to tuple
updated_tuple = tuple(list_T1)
# Printing the updated tuple
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)
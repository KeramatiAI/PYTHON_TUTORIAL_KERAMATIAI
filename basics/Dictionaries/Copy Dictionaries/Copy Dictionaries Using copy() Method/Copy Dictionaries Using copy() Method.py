"""
Copy Dictionaries Using copy() Method
Dictionaries cannot be copied directly by using the assignment operator (=), you can use the copy() method to create a shallow copy of a dictionary.

Syntax
Following is the basic syntax of the copy() method in Python −

new_dict = original_dict.copy()
Where, original_dict is the dictionary you want to copy.

Example
The following example demonstrates the creation of a shallow copy of a dictionary using the copy() method −
"""
# Creating a dictionary
dict1 = {"name": "Krishna", "age": "27", "doy": 1992}

# Copying the dictionary
dict2 = dict1.copy()

# Printing both of the dictionaries
print("dict1 :", dict1)
print("dict2 :", dict2)
"""
Output

We will get the output as shown below −

dict1 : {'name': 'Krishna', 'age': '27', 'doy': 1992}
dict2 : {'name': 'Krishna', 'age': '27', 'doy': 1992}
"""
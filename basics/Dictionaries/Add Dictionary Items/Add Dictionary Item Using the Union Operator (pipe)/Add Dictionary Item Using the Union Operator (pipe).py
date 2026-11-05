"""
Add Dictionary Item Using the Union Operator (|)
The union operator in Python, represented by the | symbol, is used to combine the elements of two sets into a new set that contains all the unique elements from both sets. It can also be used with dictionaries in Python 3.9 and later to merge the contents of two dictionaries.

We can add dictionary items using the union operator by merging two dictionaries into a new dictionary, which includes all key-value pairs from both dictionaries.

Example
In this example, we are using the | operator to combine the dictionaries "marks" and "marks1" with "marks1" values taking precedence in case of duplicate keys −
"""
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = marks | marks1
print ("marks dictionary after update: \n", newmarks)
"""
Output of the above code is as shown below −

marks dictionary before update:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 91, 'David': 49}
marks dictionary after update:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 89, 'David': 49, 'Sharad': 51, 'Mushtaq': 61}
"""
"""
Add Dictionary Item Using Unpacking
Unpacking in Python refers to extracting individual elements from a collection, such as a list, tuple, or dictionary, and assigning them to variables in a single statement. This can be done using the * operator for iterables like lists and tuples, and the ** operator for dictionaries.

We can add dictionary items using unpacking by combining two or more dictionaries with the ** unpacking operator.

Example
In the example below, we are initializing two dictionaries named "marks" and "marks1", both containing names and their corresponding integer values. Then, we create a new dictionary "newmarks" by merging "marks" and "marks1" using dictionary unpacking −
"""
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = {**marks, **marks1}
print ("marks dictionary after update: \n", newmarks)
"""
Following is the output of the above code −

marks dictionary before update:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 91, 'David': 49}
marks dictionary after update:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 89, 'David': 49, 'Sharad': 51, 'Mushtaq': 61}
"""
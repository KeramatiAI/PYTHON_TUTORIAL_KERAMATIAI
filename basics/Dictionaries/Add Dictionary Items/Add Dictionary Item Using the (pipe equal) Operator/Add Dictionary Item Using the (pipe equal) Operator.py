"""
Add Dictionary Item Using the "|=" Operator
The |= operator in Python is an in-place union operator for sets and dictionaries. It updates the set or dictionary on the left-hand side with elements from the set or dictionary on the right-hand side.

We can add dictionary items using the |= operator by updating an existing dictionary with key-value pairs from another dictionary. If there are overlapping keys, the values from the right-hand dictionary will overwrite those in the left-hand dictionary.

Example
In the following example, we use the |= operator to update "marks" with the key-value pairs from "marks1", with values from "marks1" taking precedence in case of duplicate keys −
"""
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
marks |= marks1
print ("marks dictionary after update: \n", marks)
"""
The output produced is as shown below −

marks dictionary before update:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 91, 'David': 49}
marks dictionary after update:
 {'Savita': 67, 'Imtiaz': 88, 'Laxman': 89, 'David': 49, 'Sharad': 51, 'Mushtaq': 61}
"""
"""
Add Dictionary Item Using Square Brackets
The square brackets [] in Python is used to access elements in sequences like lists and strings through indexing and slicing operations. Additionally, when working with dictionaries, square brackets are used to specify keys for accessing or modifying associated values.

You can add items to a dictionary by specifying the key within square brackets and assigning a value to it. If the key is already present in the dictionary object, its value will be updated to val. If the key is not present in the dictionary, a new key-value pair will be added.

Example
In this example, we are creating a dictionary named "marks" with keys representing names and their corresponding integer values. Then, we add a new key-value pair 'Kavta': 58 to the dictionary using square bracket notation −
"""
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("Initial dictionary: ", marks)
marks['Kavya'] = 58
print ("Dictionary after new addition: ", marks)
"""
It will produce the following output −

Initial dictionary:  {'Savita': 67, 'Imtiaz': 88, 'Laxman': 91, 'David': 49}
Dictionary after new addition:  {'Savita': 67, 'Imtiaz': 88, 'Laxman': 91, 'David': 49, 'Kavya': 58}
"""
"""
Add Dictionary Item Using the update() Method
The update() method in Python dictionaries is used to merge the contents of another dictionary or an iterable of key-value pairs into the current dictionary. It adds or updates key-value pairs, ensuring that existing keys are updated with new values and new keys are added to the dictionary.

You can add multiple items to a dictionary using the update() method by passing another dictionary or an iterable of key-value pairs.

Example
In the following example, we use the update() method to add multiple new key-value pairs 'Kavya': 58 and 'Mohan': 98 to the dictionary 'marks' −
"""
marks = {"Savita":67, "Imtiaz":88}
print ("Initial dictionary: ", marks)
marks.update({'Kavya': 58, 'Mohan': 98})
print ("Dictionary after new addition: ", marks)
"""
We get the output as shown below −

Initial dictionary:  {'Savita': 67, 'Imtiaz': 88}
Dictionary after new addition:  {'Savita': 67, 'Imtiaz': 88, 'Kavya': 58, 'Mohan': 98}
"""
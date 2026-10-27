# List to which elements will be appended
list1 = ['Fruit', 'Number', 'Animal']
# List from which elements will be appended
list2 = ['Apple', 5, 'Dog']
# Joining the lists using the append() function
for element in list2:
    list1.append(element)
# Printing the joined list
print("Joined List:", list1)
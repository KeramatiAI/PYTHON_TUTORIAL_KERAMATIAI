"""
The add() method in Python is used to add a single element to a set. If the element is already present in the set, the set remains unchanged.

We cannot directly loop through set items using the add() method because add() is used specifically to add individual elements to a set, not to iterate over existing elements.
To loop through set items, we use methods like a for loop or set comprehension.

Example
In this example, we loop through a sequence of numbers and add each number to the set using the add() method. The loop iterates over existing elements, while add() method adds new elements to the set −
"""
# Creating an empty set
my_set = set()

# Looping through a sequence and adding elements to the set
for i in range(5):
   my_set.add(i)
print(my_set)
"""
It will produce the following output −

{0, 1, 2, 3, 4}
"""
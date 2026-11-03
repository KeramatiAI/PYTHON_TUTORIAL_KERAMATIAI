"""
Iterative addition in the context of sets refers to iteratively adding elements from one set to another set using a loop or iteration construct. This allows you to merge the elements of multiple sets into a single set, ensuring that duplicate elements are not included.

We can join python sets using iterative addition by iterating over the elements of each set and adding them to a new set.

Example
In the example below, we first initialize an empty set. Then, we iterate over each element in "set1" and "set2" separately, adding each element into a new set named "joined_set" using the add() method −
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Initializing an empty set to hold the merged elements
joined_set = set()

# Iterating over set1 and adding its elements to the joined set
for element in set1:
   joined_set.add(element)

# Iterating over set2 and adding its elements to the joined set
for element in set2:
   joined_set.add(element)

print(joined_set)
"""
After executing the above code, we get the following output −

{1, 2, 3, 4, 5}
"""
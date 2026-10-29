"""
Slicing in Python is used to extract a portion of a sequence (such as a list, tuple, or string) by specifying a range of indices. The syntax for slicing is as follows −

sequence[start:stop:step]
Where,

start is the index at which the slice begins (inclusive).
stop is the index at which the slice ends (exclusive).
step is the interval between elements in the slice (optional).
We can update a tuple using slicing by creating a new tuple that includes slices of the original tuple combined with new elements.
"""
# Original tuple
T1 = (37, 14, 95, 40)
# Elements to be added
new_elements = ('green', 'blue', 'red', 'pink')
# Extracting slices of the original tuple
# Elements before index 2
part1 = T1[:2]
# Elements from index 2 onward
part2 = T1[2:]
# Create a new tuple
updated_tuple = part1 + new_elements + part2
# Printing the updated tuple
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)
"""
The slice operator in Python is used to fetch one or more items from the list. We can access list items with the slice operator by specifying the range of indices we want to extract. It uses the following syntax −

[start:stop]
Where,

start is the starting index (inclusive).
stop is the ending index (exclusive).
If we does not provide any indices, the slice operator defaults to starting from index 0 and stopping at the last item in the list.
"""
list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]
list3 = ["Rohan", "Physics", 21, 69.75]

print ("Items from index 1 to last in list1: ", list1[1:])
print ("Items from index 0 to 1 in list2: ", list2[:2])
print ("Items from index 0 to index last in list3", list3[:])
"""
Access Tuple Items with Slice Operator
The slice operator in Python is used to fetch one or more items from the tuple. We can access tuple items with the slice operator by specifying the range of indices we want to extract. It uses the following syntax −

[start:stop]
Where,

start is the starting index (inclusive).
stop is the ending index (exclusive).
"""
tuple1 = ("a", "b", "c", "d")
tuple2 = (25.50, True, -55, 1+2j)
tuple3 = (1, 2, 3, 4, 5)
tuple4 = ("Rohan", "Physics", 21, 69.75)

print ("Items from index 1 to last in tuple1: ", tuple1[1:])
print ("Items from index 0 to 1 in tuple2: ", tuple2[:2])
print ("Items from index 0 to index last in tuple3", tuple3[:])
"""
A subtuple is a part of a tuple that consists of a consecutive sequence of elements from the original tuple.

We can access a subtuple from a tuple by using the slice operator with appropriate start and stop indices. It uses the following syntax −
"""
"""my_tuple[start:stop]"""
"""
Where,

start is the starting index (inclusive).
stop is the ending index (exclusive) of the subtuple.
If we does not provide any indices, the slice operator defaults to starting from index 0 and stopping at the last item in the tuple.
"""
tuple1 = ("a", "b", "c", "d")
tuple2 = (25.50, True, -55, 1+2j)

print ("Items from index 1 to 2 in tuple1: ", tuple1[1:3])
print ("Items from index 0 to 1 in tuple2: ", tuple2[0:2])
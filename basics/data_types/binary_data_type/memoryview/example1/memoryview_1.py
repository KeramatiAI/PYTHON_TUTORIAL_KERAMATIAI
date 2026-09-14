import array
arr = array.array('i', [1, 2, 3, 4, 5])
view = memoryview(arr)

print(view)
print(type(view))
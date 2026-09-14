data = b'Hello, world!'
# Creating a view of the last part of the data
view = memoryview(data[7:])

print(view)
print(type(view))
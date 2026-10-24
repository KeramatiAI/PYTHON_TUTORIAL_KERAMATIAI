import array as ar

# initializing a string
s1 = "WORD"
print("original string:", s1, " type:", type(s1))

# converting it to an array
sar = ar.array('u', s1)
print("sar:", s1, " type:", type(sar))
# inserting an element
sar.insert(3, "L")

# getting back the modified string
s1 = sar.tounicode()
print("Modified string:", s1, " type:", type(s1))

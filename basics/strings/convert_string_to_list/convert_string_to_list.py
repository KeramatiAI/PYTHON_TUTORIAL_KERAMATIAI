s1 = "WORD"
print("original string:", s1, " type:", type(s1))
l1 = list(s1)
print("l1:", l1, " type:", type(l1))
l1.insert(3, "L")

print(l1)

s2 = ''.join(l1)
print("Modified string:", s2, " type:", type(s2))

dictionary_of_numbers = {1:10, 2:20, 3:30}
key = 2
value = 20

print(type(dictionary_of_numbers))
print("###############################################################")
print(dictionary_of_numbers.keys())
print(dictionary_of_numbers.values())

print (key, "not in", dictionary_of_numbers, ":", key not in dictionary_of_numbers)
print (key, "not in", dictionary_of_numbers, ":", key not in dictionary_of_numbers.keys())
print (value, "not in", dictionary_of_numbers, ":", value not in dictionary_of_numbers.values())
print("###############################################################")
print(dictionary_of_numbers.items())
print ((1, 10), "not in", dictionary_of_numbers, ":", (1, 10) not in dictionary_of_numbers.items())
print ((5, 50), "not in", dictionary_of_numbers, ":", (5, 50) not in dictionary_of_numbers.items())

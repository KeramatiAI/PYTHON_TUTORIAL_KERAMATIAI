dictionary_of_numbers = {1:10, 2:20, 3:30}
key = 2
value = 20

print(type(dictionary_of_numbers))
print("###############################################################")
print(dictionary_of_numbers.keys())
print(dictionary_of_numbers.values())

print (key, "in", dictionary_of_numbers, ":", key in dictionary_of_numbers)
print (key, "in", dictionary_of_numbers, ":", key in dictionary_of_numbers.keys())
print (value, "in", dictionary_of_numbers, ":", value in dictionary_of_numbers.values())
print("###############################################################")
print(dictionary_of_numbers.items())
print ((1, 10), "in", dictionary_of_numbers, ":", (1, 10) in dictionary_of_numbers.items())
print ((5, 50), "in", dictionary_of_numbers, ":", (5, 50) in dictionary_of_numbers.items())

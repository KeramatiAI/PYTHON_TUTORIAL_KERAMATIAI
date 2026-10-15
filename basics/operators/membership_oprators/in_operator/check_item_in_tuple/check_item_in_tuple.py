number_tuple = (10,20,30,40)
a = 10
b = 20

print(type(number_tuple))

print (b, "in", number_tuple, ":", b in number_tuple)

number_tuple_2 = ((10,20),30,(50,60,70))
a = 10
b = 20
c = 30
d = 40
e = 50
f = 60
g = 70
h = 80
i = 90
j = 100
print ((a,b), "in", number_tuple_2, ":", (a,b) in number_tuple_2)
print ((e,f,g), "in", number_tuple_2, ":", (e,f,g) in number_tuple_2)
print ((d,e,f), "in", number_tuple_2, ":", (d,e,f) in number_tuple_2)
a=0b101
print ("a:",a, "type:",type(a))

b=int("0b101011", 2)
print ("b:",b, "type:",type(b))
print("#####################################################")
a = "0b101"
print(a)  # output: 0b101
print("#####################################################")
a = 5
print(bin(a))  # output: 0b101
print("#####################################################")
a = 5
print(format(a, "b"))  # output: 101
#  (f-string):
print(f"{a:b}")  # output: 101
print("#####################################################")
a = 5
print(f"{a:08b}")  # output: 00000101
print("#####################################################")
a=43
b=bin(a)
print ("Integer:",a, "Binary equivalent:",b)




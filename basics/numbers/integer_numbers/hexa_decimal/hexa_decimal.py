a=0XA2
print ("a:",a, "type:",type(a))
print("#####################################################")
a = 0XA2
print(bin(a))  # output: 0b1000111 (base 2)
print("binary:",bin(a))
print(f"binary without b: {a:b}")  # output: 1000111
print("#####################################################")
a=int('0X1e', 16)
print (a, type(a))
print("#####################################################")
num_string = "A1"
number = int(num_string, 16)
print ("Hexadecimal:", num_string, "Integer:",number)
print("#####################################################")
a=hex(161)
print ("hex number: ",a," type: ", type(a))

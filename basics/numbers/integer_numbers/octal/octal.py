a=0O107
print ("a:",a, "type:",type(a))

a = 0O107
print(bin(a))  # output: 0b1000111 (base 2)
print(f"{a:b}")  # output: 1000111
print("#####################################################")
print()
a = "0O107"
binary_result = bin(int(a, 8))

print(binary_result)  # output: 0b1000111
print("#####################################################")
a=int('20',8)
print (a, type(a))
print("#####################################################")
a=0O56
print ("a:",a, "type:",type(a))

b=int("0O31",8)
print ("b:",b, "type:",type(b))

c=a+b
print ("addition:", c)
print("#####################################################")
a=oct(71)
print (a, type(a))
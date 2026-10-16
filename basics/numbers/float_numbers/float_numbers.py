a=9.99
b=0.999
c=-9.99
d=-0.999

print ("a:", a, "type", type(a))
print ("b:", b, "type", type(b))
print ("c:", c, "type", type(c))
print ("d:", d, "type", type(d))
print("######################################################")
a=float(0b10)
b=float(0O10)
c=float(0xA)

print (a,b,c, sep=",")
print ("float:",a)
print ("float:",b)
print ("float:",c)
print("######################################################")
a=float("-123.54")
b=float("1.23E04")
print ("a=",a,"b=",b)
print("######################################################")
a=1.00E400
print (a, type(a))
a=float("Infinity")
print (a, type(a))
print("######################################################")
a=float('Nan')
print(a,type(a))
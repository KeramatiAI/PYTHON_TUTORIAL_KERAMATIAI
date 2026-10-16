a=10 #decimal
b=0b10 #binary
c=0O10 #octal
d=0XA #Hexadecimal


def get_decimal(number, base=2):
    return int(str(number), base)

def get_binary(number):
    return bin(number)

def get_octal(number):
    return oct(number)

def get_hexadecimal(number):
    return hex(number).upper()


print("decimal: ",get_decimal(a)," integer: ",a)
print("binary: ",get_binary(b)," integer: ",b)
print("octal: ",get_octal(c)," integer: ",c)
print("hexadecimal: ",get_hexadecimal(d)," integer: ",d)

e=a+b+c+d
print ("summation:", e)
a=5+6j
print("number: ",a,"type: ",type(a))

a=2.25-1.2J
print("number: ",a,"type: ",type(a))

a=1.01E-2+2.2e3j
print("number: ",a,"type: ",type(a))
print("######################################################")
a=complex(5.3,6)
b=complex(1.01E-2, 2.2E3)
print ("a:", a, "type:", type(a))
print ("b:", b, "type:", type(b))
print("######################################################")
a=complex(1+2j, 2-3j)
print (a, type(a))
print("######################################################")
"""
complex(1+2j, 2-3j)
=(1+2j)+(2-3j)*j
=1+2j +2j+3
=4+4j
"""

a=complex(5.3)
print ("a:", a, "type:", type(a))
print("######################################################")
a= "5.5+2.3j"
b=complex(a)
print ("Complex number:", b)
print("######################################################")
a=5+6j
print ("Real part:", a.real, "Coefficient of Imaginary part:", a.imag)
print("######################################################")
a=5-2.2j
a.conjugate()
print(a.conjugate())

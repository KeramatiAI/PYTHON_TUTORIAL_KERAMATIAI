"""
The __annotations__ attribute itself is a dictionary in which arguments are keys and anotations their values.
"""
def myfunction(a: "physics", b:"Maths" = 20) -> int:
   c = a+b
   return c
print (myfunction.__annotations__)
"""
It will produce the following output −

{'a': 'physics', 'b': 'Maths', 'return': <class 'int'>}
"""
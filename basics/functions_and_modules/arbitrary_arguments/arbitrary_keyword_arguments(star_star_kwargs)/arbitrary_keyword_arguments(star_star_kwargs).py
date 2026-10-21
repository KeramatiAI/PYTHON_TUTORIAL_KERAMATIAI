"""
Arbitrary Keyword Arguments (**kwargs)
If a variable in the argument list has two asterisks prefixed to it, the function can accept arbitrary number of keyword arguments. The variable becomes a dictionary of keyword:value pairs.

Example
The following code is an example of a function with arbitrary keyword arguments. The addr() function has an argument **kwargs which is able to accept any number of
address elements like name, city, phno, pin, etc. Inside the function kwargs dictionary of kw:value pairs is traversed using items() method.
"""
def addr(**kwargs):
   for k,v in kwargs.items():
      print ("{}:{}".format(k,v))

print ("pass two keyword args")
addr(Name="John", City="Mumbai")
print ("pass four keyword args")

# pass four keyword args
addr(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")
"""
It will produce the following output −

pass two keyword args
Name:John
City:Mumbai
pass four keyword args
Name:Raam
City:Mumbai
ph_no:9123134567
PIN:400001
"""
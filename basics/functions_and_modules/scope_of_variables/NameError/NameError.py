"""
Lastly, if you try to access a local variable in global scope, Python raises NameError as the variable in local scope can't be accessed outside it.
"""
var1 = 50 # this is a global variable
var2 = 60 # this is a global variable
def myfunction(x, y):
   total = x+y
   print ("Total is a local variable: ", total)

myfunction(var1, var2)
print (total) # This gives NameError
"""
It will produce the following error message −

Total is a local variable: 110
Traceback (most recent call last):

   print (total) # This gives NameError
          ^^^^^
NameError: name 'total' is not defined
"""
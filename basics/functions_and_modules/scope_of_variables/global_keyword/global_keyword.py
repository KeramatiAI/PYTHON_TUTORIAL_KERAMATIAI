"""
To modify a global variable, you can either update it with a dictionary syntax, or use the global keyword to refer it before modifying.
"""
var1 = 50 # this is a global variable
var2 = 60 # this is a global variable
def myfunction():
   "Change values of global variables"
   globals()['var1'] = globals()['var1']+10
   global var2
   var2 = var2 + 20

myfunction()
print ("var1:",var1, "var2:",var2) #shows global variables with changed values
"""
On executing the code, it will produce the following output −

var1: 60 var2: 80
"""
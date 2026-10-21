"""
If you try to manipulate value of a global variable from inside a function, Python raises UnboundLocalError as shown in example below −
"""
# this is a global variable
marks = 50
def myfunction():
   marks = marks + 20
   print (marks)

myfunction()
# prints global value
print (marks)
"""
It will produce the following error message −

   marks = marks + 20
           ^^^^^
UnboundLocalError: cannot access local variable 'marks' where it is not associated with a value
"""
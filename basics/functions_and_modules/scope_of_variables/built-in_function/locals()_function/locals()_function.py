"""
Python locals() Function
Python's standard library includes a built-in function locals(). It returns a dictionary of symbols currently available in the local namespace of the function.

Example
Modify the above script to print dictionary of global and local namespaces from within the function.
"""
name = 'Davoud Keramati'
marks = 50
result = True
def myfunction():
   a = 10
   b = 20
   c = a+b
   print ("globals():", globals())
   print ("locals():", locals())
   return c
myfunction()
"""
The output shows that locals() returns a dictionary of variables and their values currently available in the function.

globals(): {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000169AE265250>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\mlath\\examples\\main.py', '__cached__': None, 'name': 'TutorialsPoint', 'marks': 50, 'result': True, 'myfunction': <function myfunction at 0x00000169AE2104A0>}
locals(): {'a': 10, 'b': 20, 'c': 30}
Since both globals() and locals functions return dictionary, you can access value of a variable from respective namespace with dictionary get() method or index operator.
"""
print (globals()['name']) # displays TutorialsPoint
print (locals().get('a')) # displays 10
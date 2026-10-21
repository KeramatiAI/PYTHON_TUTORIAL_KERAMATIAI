"""
Python globals() Function
Python's standard library includes a built-in function globals(). It returns a dictionary of symbols currently available in global namespace.

Run the globals() function directly from the Python prompt.

>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
It can be seen that the built-in module which contains definitions of all built-in functions and built-in exceptions is loaded.
"""
name = 'Davoud Keramati'
marks = 50
result = True


def myfunction():
    a = 10
    b = 20
    return a + b


print(globals())
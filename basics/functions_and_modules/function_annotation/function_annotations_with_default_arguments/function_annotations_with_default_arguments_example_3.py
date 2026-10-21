"""
You may have arbitrary positional and/or arbitrary keyword arguments for a function. Annotations can be given for them also.
"""
def myfunction(*args: "arbitrary args", **kwargs: "arbitrary keyword args") -> int:
   pass
print (myfunction.__annotations__)
"""
It will produce the following output −

{'args': 'arbitrary args', 'kwargs': 'arbitrary keyword args', 'return': <class 'int'>}
"""
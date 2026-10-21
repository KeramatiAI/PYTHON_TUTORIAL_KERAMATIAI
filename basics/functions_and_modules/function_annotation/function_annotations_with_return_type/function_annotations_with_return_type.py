"""
Annotations are ignored at runtime, but are helpful for the IDEs and static type checker libraries such as mypy.

You can give annotation for the return data type as well. After the parentheses and before the colon symbol, put an arrow (->) followed by the annotation.

Example
In this example, we are providing annotation for return type.
"""
def myfunction(a: int, b: int) -> int:
   c = a+b
   return c
print(myfunction(56,88))
print(myfunction.__annotations__)
"""
This will generate the following output −

144
{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
"""
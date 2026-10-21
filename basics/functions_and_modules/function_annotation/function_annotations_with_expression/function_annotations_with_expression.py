"""
Function Annotations With Expression
As using the data type as annotation is ignored at runtime, you can put any expression which acts as the metadata for the arguments. Hence, function may have any arbitrary expression as annotation.

Example
In the below example, we are using expression as a function annotation.
"""
def total(x : 'marks in Physics', y: 'marks in chemistry'):
   return x+y
print(total(86, 88))
print(total.__annotations__)
"""
Following is the output −

174
{'x': 'marks in Physics', 'y': 'marks in chemistry'}
"""
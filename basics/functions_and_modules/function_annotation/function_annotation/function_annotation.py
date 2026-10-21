"""
Remember that Python is a dynamically typed language, and doesn't enforce any type checking at runtime. Hence annotating the arguments with data types doesn't have any effect while calling the function.
Even if non-integer arguments are given, Python doesn't detect any error.
"""
def myfunction(a: int, b: int):
    c = a + b
    return c


print(myfunction(10, 20))
print(myfunction("Hello ", "Python"))
"""
It will produce the following output −

30
Hello Python
"""
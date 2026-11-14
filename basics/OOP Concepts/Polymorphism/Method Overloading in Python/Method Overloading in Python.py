"""
Method Overloading in Python
When a class contains two or more methods with the same name but different number of parameters then this scenario can be termed as method overloading.

Python does not allow overloading of methods by default, however, we can use the techniques like variable-length argument lists, multiple dispatch and default parameters to achieve this.

Example
In the following example, we are using the variable-length argument lists to achieve method overloading.
"""
def add(*nums):
   return sum(nums)

# Call the function with different number of parameters
result1 = add(10, 25)
result2 = add(10, 25, 35)

print(result1)
print(result2)
"""
When the above code is executed, it produces the following result −

35
70
"""
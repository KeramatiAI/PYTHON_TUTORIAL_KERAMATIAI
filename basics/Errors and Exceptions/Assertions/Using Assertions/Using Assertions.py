"""Using Assertions
Assertions are generally used during development and testing phases to check conditions that should always hold true.

Example
In the following example, we are using assertions to ensure that the variable "num" falls within the valid range of "0" to "100". If the assertion fails, Python raises an "AssertionError", preventing further execution of the subsequent print statement −
"""
print('Enter marks out of 100:')
num = 75
assert num >= 0 and num <= 100
print('Marks obtained:', num)

num = 125
assert num >= 0 and num <= 100
print('Marks obtained:', num)  # This line won't be reached if assertion fails
"""Following is the output of the above code −

Enter marks out of 100:
Marks obtained: 75
Traceback (most recent call last):
  File "/home/cg/root/66723bd115007/main.py", line 7, in <module>
    assert num >= 0 and num <= 100
AssertionError"""
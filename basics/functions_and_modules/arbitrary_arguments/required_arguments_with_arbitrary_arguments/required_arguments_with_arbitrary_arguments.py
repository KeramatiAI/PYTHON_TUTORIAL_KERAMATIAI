"""
It is also possible to have a function with some required arguments before the sequence of variable number of values.

Example
The following example has avg() function. Assume that a student can take any number of tests. First test is mandatory. He can take as many tests as he likes to better his score. The function calculates the average of marks in first test and his maximum score in the rest of tests.

The function has two arguments, first is the required argument and second to hold any number of values.
"""
# avg of first test and best of following tests
def avg(first, *rest):
    second = max(rest)
    return (first + second) / 2


result = avg(40, 30, 50, 25)
print(result)
"""
Following call to avg() function passes first value to the required argument first, and the remaining values to a tuple named rest. We then find the maximum and use it to calculate the average.

It will produce the following output −

45.0
"""

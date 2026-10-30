"""
The ** (double star) operator is used to unpack the fields of the namedtuple into keyword arguments. This can be useful when you want to pass the fields of a namedtuple to a function that accepts keyword arguments.

The following example demonstrates how to use the ** operator −
"""
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student',
                                 ['name', 'age', 'DOB'])

# Adding values
S = Student('farhan', '23', '2541997')

# initializing iterable
li = ['nishu', '19', '411997']

# initializing dict
di = {'name': "ravi", 'age': 24, 'DOB': '1391997'}

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))
"""
The output of the above code will be −

The namedtuple instance from dict is  :
Student(name='ravi', age=24, DOB='1391997')
"""
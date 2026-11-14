"""
Implement Method Overloading Using MultipleDispatch
Python's standard library doesn't have any other provision for implementing method overloading. However, we can use a dispatch function from a third-party module named MultipleDispatch for this purpose.

First, you need to install the Multipledispatch module using the following command −

pip install multipledispatch
This module has a @dispatch decorator. It takes the number of arguments to be passed to the method to be overloaded. Define multiple copies of add() method with @dispatch decorator as below −
"""
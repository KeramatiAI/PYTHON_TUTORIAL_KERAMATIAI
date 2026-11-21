"""
User-Defined Exceptions in Python
User-defined exceptions in Python are custom error classes that you create to handle specific error conditions in your code. They are derived from the built-in Exception class or any of its sub classes.

User-defined exceptions provide more precise control over error handling in your application −

Clarity − They provide specific error messages that make it clear what went wrong.

Granularity − They allow you to handle different error conditions separately.

Maintainability − They centralize error handling logic, making your code easier to maintain.

How to Create a User-Defined Exception
To create a user-defined exception, follow these steps −

Step 1 − Define the Exception Class
Create a new class that inherits from the built-in "Exception" class or any other appropriate base class. This new class will serve as your custom exception.

class MyCustomError(Exception):
   pass
Explanation

Inheritance − By inheriting from "Exception", your custom exception will have the same behaviour and attributes as the built-in exceptions.

Class Definition − The class is defined using the standard Python class syntax. For simple custom exceptions, you can define an empty class body using the "pass" statement.
"""
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

Step 2 − Initialize the Exception
Implement the "__init__" method to initialize any attributes or provide custom error messages. This allows you to pass specific information about the error when raising the exception.

class InvalidAgeError(Exception):
   def __init__(self, age, message="Age must be between 18 and 100"):
      self.age = age
      self.message = message
      super().__init__(self.message)
Explanation

Attributes − Define attributes such as "age" and "message" to store information about the error.

Initialization − The "__init__" method initializes these attributes. The "super().__init__(self.message)" call ensures that the base "Exception" class is properly initialized with the error message.

Default Message − A default message is provided, but you can override it when raising the exception.

Step 3 − Optionally Override "__str__" or "__repr__"
Override the "__str__" or "__repr__" method to provide a custom string representation of the exception. This is useful for printing or logging the exception.

class InvalidAgeError(Exception):
   def __init__(self, age, message="Age must be between 18 and 100"):
      self.age = age
      self.message = message
      super().__init__(self.message)

   def __str__(self):
      return f"{self.message}. Provided age: {self.age}"
Explanation

__str__ Method − The "__str__" method returns a string representation of the exception. This is what will be displayed when the exception is printed.

Custom Message − Customize the message to include relevant information, such as the provided age in this example.
"""
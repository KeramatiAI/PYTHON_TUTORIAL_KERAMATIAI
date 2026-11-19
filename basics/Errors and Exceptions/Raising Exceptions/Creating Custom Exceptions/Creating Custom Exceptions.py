"""Creating Custom Exceptions
Custom exceptions is useful for handling specific error conditions that are unique to your application, providing more precise error reporting and control.

To create a custom exception in Python, you define a new class that inherits from the built-in Exception class or any other appropriate built-in exception class. This custom exception class can have additional attributes and methods to provide more detailed context about the error condition.

Example
In this example −

We define a custom exception class "InvalidAgeError" that inherits from "Exception".
The __init__() method initializes the exception with the invalid age and a default error message.
The set_age() function raises "InvalidAgeError" if the provided age is outside the valid range."""
class InvalidAgeError(Exception):
   def __init__(self, age, message="Age must be between 18 and 100"):
      self.age = age
      self.message = message
      super().__init__(self.message)

def set_age(age):
   if age < 18 or age > 100:
      raise InvalidAgeError(age)
   print(f"Age is set to {age}")

try:
   set_age(150)
except InvalidAgeError as e:
   print(f"Invalid age: {e.age}. {e.message}")
"""The result obtained is as shown below −

Invalid age: 150. Age must be between 18 and 100"""
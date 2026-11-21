"""
Assertions in Python
Assertions in Python are statements that assert or assume a condition to be true. If the condition turns out to be false, Python raises an AssertionError exception. They are used to detect programming errors that should never occur if the code is correct.

The easiest way to think of an assertion is to liken it to a raise-if statement (or to be more accurate, a raise-if-not statement). An expression is tested, and if the result comes up false, an exception is raised.

Assertions are carried out by the assert statement, the newest keyword to Python, introduced in version 1.5.

Programmers often place assertions at the start of a function to check for valid input, and after a function call to check for valid output.

The assert Statement
In Python, assertions use the assert keyword followed by an expression. If the expression evaluates to False, an AssertionError is raised. Following is the syntax of assertion −

assert condition, message
Where,

condition − A boolean expression that should be true.

message (optional) − An optional message to be displayed if the assertion fails.
"""
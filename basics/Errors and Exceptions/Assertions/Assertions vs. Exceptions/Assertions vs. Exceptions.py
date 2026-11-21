"""
Assertions vs. Exceptions
Assertions are used to check internal state and invariants that should always be true. Whereas, exceptions helps in handling runtime errors and exceptional conditions that may occur during normal execution.

Assertions are disabled by default in Python's optimized mode (-O or python -O script.py). Therefore, they should not be used to enforce constraints that are required for the correct functioning of the program in production environments.
"""
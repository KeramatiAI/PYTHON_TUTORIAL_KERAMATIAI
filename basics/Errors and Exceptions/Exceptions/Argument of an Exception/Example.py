"""Example"""
"""Following is an example for a single exception −"""

# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print ("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz")
"""This produces the following result −

The argument does not contain numbers
invalid literal for int() with base 10: 'xyz'"""
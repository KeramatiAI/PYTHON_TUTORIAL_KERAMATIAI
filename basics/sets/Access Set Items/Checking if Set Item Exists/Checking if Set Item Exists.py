"""
You can check whether a certain item is available in the set using the Python's membership operators, in and not in.

The in operator returns True if the specified element is found within the collection, and False otherwise. Conversely, the not in operator returns True if the element is not present in the collection, and False if it is.

Example
In the below example, the "in" operator verifies whether the item "Java" exists in the set "langs", and the "not in" operator checks whether the item "SQL" does not exist in the set −
"""
# Defining a set
langs = {"C", "C++", "Java", "Python"}

# Checking if an item exists in the set
if "Java" in langs:
    print("Java is present in the set.")
else:
    print("Java is not present in the set.")

# Checking if an item does not exist in the set
if "SQL" not in langs:
    print("SQL is not present in the set.")
else:
    print("SQL is present in the set.")
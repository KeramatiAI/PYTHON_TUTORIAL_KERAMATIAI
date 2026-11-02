"""
Example
If we try to remove element from an empty set, the pop() method will raise a KeyError exception −
"""
# Defining an empty set
empty_set = set()

# Removing an arbitrary element from the empty set
removed_element = empty_set.pop()
"""
The error produced is as shown below −

Traceback (most recent call last):
  File "/home/cg/root/664c69620cd40/main.py", line 5, in <module>
removed_element = empty_set.pop()
KeyError: 'pop from an empty set'
"""
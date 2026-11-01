"""Mathematically, a subset is a set that contains only elements that are also contained in another set. In other words, every element of the subset is also an element of the original set. If every element of set A is also an element of set B, then A is considered a subset of B, denoted as A ⊆ B.

In Python, you can access subsets from a set using set operations or by iterating over the power set (the set of all subsets) and filtering based on specific criteria.

Using Set Operations − You can use built-in set operations such as issubset() function to check if one set is a subset of another.

Iterating Over Power Set − Iterate over all possible subsets of the set and filter based on certain criteria to access specific subsets.

Example
Following is the basic example demonstrating how to access subsets from a set −"""
import itertools

# Defining a set
original_set = {1, 2, 3, 4}

# Checking if {1, 2} is a subset of the original set
is_subset = {1, 2}.issubset(original_set)
print("{1, 2} is a subset of the original set:", is_subset)

# Generating all subsets with two elements
subsets_with_two_elements = [set(subset) for subset in itertools.combinations(original_set, 2)]
print("Subsets with two elements:", subsets_with_two_elements)
"""
Following is the output of the above code −

{1, 2} is a subset of the original set: True
Subsets with two elements: [{1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}]
"""
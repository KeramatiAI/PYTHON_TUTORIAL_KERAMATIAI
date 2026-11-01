"""
In Python, the union operator (|) is used to perform a union operation between two sets. The union of two sets contains all the distinct elements present in either of the sets, without any duplicates.

We can add set items using the union operator by performing the union operation between two sets using the "|" operator or union() function, which combines the elements from both sets into a new set, containing all unique elements present in either of the original sets.

Example
The following example combine sets using the union() method and the | operator to create new sets containing unique elements from the original sets −
"""
# Defining three sets
lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang3 = {"SQL", "C#"}

# Performing union operation
combined_set1 = lang1.union(lang2)
combined_set2 = lang2 | lang3

# Print the combined set
print ("Combined Set1:", combined_set1)
print("Combined Set2:", combined_set2)
"""
Output of the above code is as shown below −

Combined Set1: {'C#', 'Perl', 'C++', 'Java', 'PHP', 'Python', 'C'}
Combined Set2: {'C#', 'Perl', 'PHP', 'SQL'}
"""
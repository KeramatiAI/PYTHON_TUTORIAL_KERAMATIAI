"""
The copy() method in set class is used to create a shallow copy of a set object.

A shallow copy means that the method creates a new collection object, but does not create copies of the objects contained within the original collection. Instead, it copies the references to these objects.

Therefore, if the original collection contains mutable objects (like lists, dictionaries, or other sets), modifications to these objects will be reflected in both the original and the copied collections.

Syntax
Following is the syntax of the copy() method −

set.copy()
Return Value
The copy() method returns a new set which is a shallow copy of existing set.

Example
In the following example, we are creating a copy of the set "lang1" and storing it in "lang2", then retrieving both sets and their memory addresses using id().

After adding an element to "lang1", we retrieve both sets and their memory addresses again to show that "lang1" and "lang2" are independent copies −
"""
lang1 = {"C", "C++", "Java", "Python"}
print ("lang1: ", lang1, "id(lang1): ", id(lang1))
lang2 = lang1.copy()
print ("lang2: ", lang2, "id(lang2): ", id(lang2))
lang1.add("PHP")
print ("After updating lang1")
print ("lang1: ", lang1, "id(lang1): ", id(lang1))
print ("lang2: ", lang2, "id(lang2): ", id(lang2))
"""
Output

This will produce the following output −

lang1: {'Python', 'Java', 'C', 'C++'} id(lang1): 2451578196864
lang2: {'Python', 'Java', 'C', 'C++'} id(lang2): 2451578197312
After updating lang1
lang1: {'Python', 'C', 'C++', 'PHP', 'Java'} id(lang1): 2451578196864
lang2: {'Python', 'Java', 'C', 'C++'} id(lang2): 2451578197312
"""
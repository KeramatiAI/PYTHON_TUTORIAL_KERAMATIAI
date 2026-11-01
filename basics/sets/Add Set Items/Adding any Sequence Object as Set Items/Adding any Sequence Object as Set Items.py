"""
Adding any Sequence Object as Set Items
The update() method also accepts any sequence object as argument.

In this example, we first define a set and a tuple, lang1 and lang2, containing different programming languages. Then, we add all elements from "lang2" to "lang1" using the update() method −
"""
# Defining a set
lang1 = {"C", "C++", "Java", "Python"}
# Defining a tuple
lang2 = {"PHP", "C#", "Perl"}
lang1.update(lang2)
print (lang1)
"""
The result obtained is as shown below −

{'Python', 'C++', 'C#', 'C', 'Java', 'PHP', 'Perl'}
"""
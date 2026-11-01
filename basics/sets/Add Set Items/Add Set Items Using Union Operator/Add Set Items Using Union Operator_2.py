"""
If a sequence object is given as argument to union() method, Python automatically converts it to a set first and then performs union −
"""
lang1 = {"C", "C++", "Java", "Python"}
lang2 = ["PHP", "C#", "Perl"]
lang3 = lang1.union(lang2)
print (lang3)
"""
The output produced is as follows −

{'PHP', 'C#', 'Python', 'C', 'Java', 'C++', 'Perl'}
"""
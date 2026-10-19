"""
Python Nested while Loop Syntax
The syntax for a nested while loop statement in Python programming language is as follows −

while expression:
   while expression:
      statement(s)
   statement(s)
"""
i = 2
while(i < 25):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print (i, " is prime")
   i = i + 1

print ("Good bye!")
"""
2 is prime
3 is prime
5 is prime
7 is prime
11 is prime
13 is prime
17 is prime
19 is prime
23 is prime
Good bye!
"""
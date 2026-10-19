"""
Syntax of continue Statement

looping statement:
   condition check:
      continue
"""
for letter in 'Python':
   if letter == 'h':
      continue
   print ('Current Letter :', letter)
print ("Good bye!")

"""
output:
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : o
Current Letter : n
Good bye!
"""
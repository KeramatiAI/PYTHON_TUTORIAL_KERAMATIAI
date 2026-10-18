"""
Syntax of For Else Loop
Following is the syntax of for loop with optional else block −

for variable_name in iterable:
 #stmts in the loop
 .
 .
 .
else:
 #stmts in else clause
 .
 .
"""
for count in range(6):
   print ("Iteration no. {}".format(count))
else:
   print ("for loop over. Now in else block")
print ("End of for loop")
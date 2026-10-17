"""
if boolean_expression1:
   statement(s)
   if boolean_expression2:
      statement(s)
"""
num = 36
print ("num = ", num)
if num % 2 == 0:
   if num % 3 == 0:
      print ("Divisible by 3 and 2")
print("....execution ends....")

"""
if expression1:
   statement(s)
   if expression2:
      statement(s)
   else
      statement(s)
else:
   if expression3:
      statement(s)
   else:
      statement(s)
"""
num=8
print ("num = ",num)
if num%2==0:
   if num%3==0:
      print ("Divisible by 3 and 2")
   else:
      print ("divisible by 2 not divisible by 3")
else:
   if num%3==0:
      print ("divisible by 3 not divisible by 2")
   else:
      print ("not Divisible by 2 not divisible by 3")
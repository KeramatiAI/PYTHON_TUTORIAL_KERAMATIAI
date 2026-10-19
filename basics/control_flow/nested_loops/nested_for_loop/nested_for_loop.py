"""
Python Nested for Loop Syntax
The syntax for a Python nested for loop statement in Python programming language is as follows −

for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)
"""
months = ["jan", "feb", "mar"]
days = ["sun", "mon", "tue"]

for x in months:
  for y in days:
    print(x, y)

print("Good bye!")
"""
output:
jan sun
jan mon
jan tue
feb sun
feb mon
feb tue
mar sun
mar mon
mar tue
Good bye!
"""
"""
Multiple Inheritance
Multiple inheritance in Python allows you to construct a class based on more than one parent classes. The Child class thus inherits the attributes and method from all parents. The child can override methods inherited from any parent.

Syntax
class parent1:
   #statements

class parent2:
   #statements

class child(parent1, parent2):
   #statements
Example
Python's standard library has a built-in divmod() function that returns a two-item tuple. First number is the division of two arguments, the second is the mod value of the two operands.

This example tries to emulate the divmod() function. We define two classes division and modulus, and then have a div_mod class that inherits them.
"""
class division:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def divide(self):
      return self.n/self.d
class modulus:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def mod_divide(self):
      return self.n%self.d

class div_mod(division,modulus):
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def div_and_mod(self):
      divval=division.divide(self)
      modval=modulus.mod_divide(self)
      return (divval, modval)
"""
The child class has a new method div_and_mod() which internally calls the divide() and mod_divide() methods from its inherited classes to return the division and mod values.

x=div_mod(10,3)
print ("division:",x.divide())
print ("mod_division:",x.mod_divide())
print ("divmod:",x.div_and_mod())
Output
division: 3.3333333333333335
mod_division: 1
divmod: (3.3333333333333335, 1)
"""
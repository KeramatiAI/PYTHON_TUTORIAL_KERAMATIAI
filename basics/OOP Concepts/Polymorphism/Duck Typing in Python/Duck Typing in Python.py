"""
Duck Typing in Python
Duck typing is a concept where the type or class of an object is less important than the methods it defines. Using this concept, you can call any method on an object without checking its type, as long as the method exists.

This term is defined by a very famous quote that states: Suppose there is a bird that walks like a duck, swims like a duck, looks like a duck, and quaks like a duck then it probably is a duck.

Example
In the code given below, we are practically demonstrating the concept of duck typing.
"""
class Duck:
   def sound(self):
      return "Quack, quack!"

class AnotherBird:
   def sound(self):
      return "I'm similar to a duck!"

def makeSound(duck):
   print(duck.sound())

# creating instances
duck = Duck()
anotherBird = AnotherBird()
# calling methods
makeSound(duck)
makeSound(anotherBird)
"""
When you execute this code, it will produce the following output −

Quack, quack!
I'm similar to a duck!
"""
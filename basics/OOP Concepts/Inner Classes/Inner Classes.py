"""
Inner Class in Python

A class defined inside another class is known as an inner class in Python. Sometimes inner class is also called nested class. If the inner class is instantiated, the object of inner class can also be used by the parent class. Object of inner class becomes one of the attributes of the outer class. Inner class automatically inherits the attributes of the outer class without formally establishing inheritance.

Syntax
class outer:
   def __init__(self):
      pass
   class inner:
      def __init__(self):
         pass
An inner class lets you group classes. One of the advantages of nesting classes is that it becomes easy to understand which classes are related. The inner class has a local scope. It acts as one of the attributes of the outer class.

Example
In the following code, we have student as the outer class and subjects as the inner class. The __init__() constructor of student initializes name attribute and an instance of subjects class. On the other hand, the constructor of inner subjects class initializes two instance variables sub1, sub2.

A show() method of outer class calls the method of inner class with the object that has been instantiated.
"""


class student:
    def __init__(self):
        self.name = "Ashish"
        self.subs = self.subjects()
        return

    def show(self):
        print("Name:", self.name)
        self.subs.display()

    class subjects:
        def __init__(self):
            self.sub1 = "Phy"
            self.sub2 = "Che"
            return

        def display(self):
            print("Subjects:", self.sub1, self.sub2)


s1 = student()
s1.show()

"""
When you execute this code, it will produce the following output −

Name: Ashish
Subjects: Phy Che
It is quite possible to declare an object of outer class independently, and make it call its own display() method.

sub = student().subjects().display()
It will list out the subjects.

Types of Inner Class
In Python, inner classes are of two types −

Multiple Inner Class
Multilevel Inner Class
"""
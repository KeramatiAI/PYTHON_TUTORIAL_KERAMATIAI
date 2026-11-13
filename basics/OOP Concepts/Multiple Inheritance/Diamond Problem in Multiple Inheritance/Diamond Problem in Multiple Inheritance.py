"""
Diamond Problem in Multiple Inheritance
The diamond problem is a common issue in multiple inheritance. It arises when two parent classes inherit from the same base class, and a child class inherits from both parent classes. The diagram below shows this scenario:

Diamond Problem Diagram
The diamond problem creates a confusion that which method to call from the base class when it is inherited by the child class. Python resolves this by following a the mro (Method Resolution Order) that we discussed earlier. Let's see an example of the diamond problem −

Example
The code below demonstrates the diamond problem and how Python resolves it using MRO −
"""
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.show()
"""
The output of the above code will be −

Class B
Explanation: The MRO order for class D is [D, B, C, A]. So, when d.show() is called, it first looks in class D, no show function is found there, so it goes to class B, finds the show function, and executes it.


"""
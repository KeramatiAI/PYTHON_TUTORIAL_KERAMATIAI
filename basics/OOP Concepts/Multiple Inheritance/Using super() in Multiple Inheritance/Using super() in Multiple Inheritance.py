"""
Using super() in Multiple Inheritance
The super() function is used by child class to call a method from a parent class. If you use super() in a method in the case of multiple inheritance, it will strictly follow the MRO order to determine which method to call.

Example
In this example, we have a class hierarchy with four classes: A, B, C, and D. Class D inherits from both B and C, demonstrating multiple inheritance.
"""
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")
        super().show()

class C(A):
    def show(self):
        print("Class C")
        super().show()

class D(B, C):
    def show(self):
        print("Class D")
        super().show()

d = D()
d.show()
"""
The output of the above code will be −

Class D
Class B
Class C
Class A
Explanation: The MRO for class D is [D, B, C, A, object]. This means that when a method is called on an instance of D, Python will look for the method in D first, then B, then C, and finally A. So, "Class D", "Class B", "Class C", and "Class A" will be printed in that order.


"""
"""
Example of Multiple Inheritance
In the following example, the Child class inherits from both the Father and Mother classes −
"""
class Father:
    def skill1(self):
        print("Father's skill: Gardening")

class Mother:
    def skill2(self):
        print("Mother's skill: Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill1()
c.skill2()
"""
The output of above code will be −

Father's skill: Gardening
Mother's skill: Cooking
Explanation: In this example, the Child class have access to both skill1() and skill2() methods from its parent classes. When we create an instance of Child and call skill1(), it executes the method from the Father class. Similarly, when we call skill2(), it executes the method from the Mother class.

But, what will happen if both parent classes have a method with the same name? Which will be executed? This is where the method resolution order (MRO) comes into play.
"""
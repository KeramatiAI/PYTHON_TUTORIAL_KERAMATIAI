"""
Method Resolution Order for Multiple Inheritance
If methods with same name are defined in multiple parent classes, Python follows a specific order to decide which method to execute. This order is known as the Method Resolution Order (MRO). This order is determined by the C3 linearization algorithm, also called MRO. The MRO order is listed below.

First, Python looks for the method in the child class itself.
If not found, it searches the parent classes in the order they are listed.
This continues until the method is found or all classes have been searched.
You can check the MRO of a object using the mro() method or the __mro__ attribute. For example −

print(Child.mro())

Output:
[<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>,
<class 'object'>]
Example
In the following example, the Child class inherits skill() method from both the Father and Mother classes, but mother's method is called.
"""
class Father:
    def skill(self):
        print("Father's skill: Gardening")

class Mother:
    def skill(self):
        print("Mother's skill: Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill()
"""
Explanation: When the skill method is called on the Child class instance c, it will first look for the method in the Child class. Since the Child class does not have a skill method, it will search the parent classes in the order they are listed (Father, then Mother) and execute the first one it finds.

The output of above code will be −

Father's skill: Gardening
"""
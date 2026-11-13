"""
Overriding Methods in Multilevel Inheritance
In multilevel inheritance, a derived class can override methods of its parent class. Meaning, if a method is defined in both the parent class and the child class, the method in the child class will override the one in the parent class.

Here's an example to illustrate method overriding in multilevel inheritance −
"""
# Base class
class Vehicle:
    def start(self):
        return "Vehicle starts"

# Derived class
class Car(Vehicle):
    def start(self):
        return "Car starts"

# Sub-derived class
class SportsCar(Car):
    def start(self):
        return "Sports Car starts"

# Creating an instance of SportsCar
sports_car = SportsCar()
print(sports_car.start())  # Calls the start method of SportsCar class
"""
The output of the above code will be −

Sports Car starts
Conclusion
To conclude, multilevel inheritance is a type of inheritance where a class is derived from another derived class such that a chain of inheritance is formed. The method resolution order (MRO) will determine which method is called when there are methods with the same name in the inheritance chain. Method overriding can be performed to override the methods of the parent class in the child class.
"""
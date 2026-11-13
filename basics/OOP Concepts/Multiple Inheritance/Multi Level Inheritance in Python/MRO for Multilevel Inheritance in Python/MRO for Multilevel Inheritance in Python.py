"""
MRO for Multilevel Inheritance in Python
Let's consider a scenario from the above example in which the Network_5G class also have a method named connectivity(). Now, What will happen if we call the connectivity() method from the instance of the Network_5G_Airtel class?. This is where the Method Resolution Order (MRO) comes into play.

Let's modify the previous example to include a connectivity() method in the Network_5G class −
"""
# Base class
class Network:
    def connectivity(self):
        return "Network connects"

# Derived class
class Network_5G(Network):
    def fast_connectivity(self):
        return "5G Network provides superfast connectivity"

    def connectivity(self):
        return "5G Network connects faster"

# Sub-derived class
class Network_5G_Airtel(Network_5G):
    def fast_and_stable_connectivity(self):
        return "Airtel 5G network is fast and remains stable"

# Creating an instance of Network_5G_Airtel
obj1 = Network_5G_Airtel()
print(obj1.connectivity())  # Inherited from Network class
"""
The output of the above code will be −

5G Network connects faster
This shows that the connectivity() method from the Network_5G class is called instead of the one from the Network class. This is because the method resolution order (MRO) in Python follows a depth-first approach, meaning it will first look for the method in the current class, then in the parent class, and so on up the hierarchy.

To know the method resolution order of any class, you can use the mro() method. Here's how you can do it:

print(Network_5G_Airtel.mro())

Output:
[<class '__main__.Network_5G_Airtel'>, <class '__main__.Network_5G'>, 
<class '__main__.Network'>, <class 'object'>]
"""
"""
Example of Multilevel Inheritance in Python
Let's look at an example to understand how multilevel inheritance works in Python −
"""
# Base class
class Network:
    def connectivity(self):
        return "Network connects"

# Derived class
class Network_5G(Network):
    def fast_connectivity(self):
        return "5G Network provides superfast connectivity"

# Sub-derived class
class Network_5G_Airtel(Network_5G):
    def fast_and_stable_connectivity(self):
        return "Airtel 5G network is fast and remains stable"

# Creating an instance of Network_5G_Airtel
network_object = Network_5G_Airtel()
print(network_object.connectivity())        # Inherited from Network class
print(network_object.fast_connectivity())   # Inherited from Network_5G class
print(network_object.fast_and_stable_connectivity())   # Inherited from Network_5G_Airtel class
"""
In this code, the Network_5G_Airtel class inherits the functions and attributes from the Network_5G class, which in turn inherits from the Network class. So the Network_5G_Airtel will have access to methods such as connectivity()(from Network), fast_connectivity()(from Network_5G), and fast_and_stable_connectivity()(from Network_5G_Airtel itself).

When you run the code, its output will be −

Network connects
5G Network provides superfast connectivity
Airtel 5G network is fast and remains stable
"""
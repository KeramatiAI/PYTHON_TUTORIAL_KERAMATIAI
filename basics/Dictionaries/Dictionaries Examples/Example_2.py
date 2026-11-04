"""
Example 2
Python doesn't accept unhashable objects such as list as key, and raises TypeError.
"""
d1 = {["Mango","Banana"]:"Fruit", "Flower":["Rose", "Lotus"]} # TypeError: unhashable type: 'list'
print (d1)
"""
It will raise a TypeError −

Traceback (most recent call last):
   
d1 = {["Mango","Banana"]:"Fruit", "Flower":["Rose", "Lotus"]}
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'
"""
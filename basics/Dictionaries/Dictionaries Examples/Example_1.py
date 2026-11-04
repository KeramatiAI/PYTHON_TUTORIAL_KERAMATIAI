"""
Example 1
Only hashable objects can be used as keys, such as a number, string or tuple (containing only hashable elements). You can use an object of any type as the value. Hence following definitions of dictionary are also valid −
"""
d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)
"""
It will produce the following output −

{'Fruit': ['Mango', 'Banana'], 'Flower': ['Rose', 'Lotus']}
{'India, USA': 'Countries', ('New Delhi', 'New York'): 'Capitals'}
"""
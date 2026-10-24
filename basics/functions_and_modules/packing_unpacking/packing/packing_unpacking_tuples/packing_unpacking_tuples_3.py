tuple_1 = (10,20,30,40,50,60)
print(type(tuple_1))

*x, y, z = tuple_1
print ("x: ",x, "y: ", y, "z: ", z)

print("x:",x," type:",type(x))
print("y:",z," type:",type(y))
print("z:",x," type:",type(z))
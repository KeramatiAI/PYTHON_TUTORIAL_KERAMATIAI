"""
In case you need to provide more than one annotation expressions to a function argument, give it in the form of a dictionary object in front of the argument itself.
"""
def division(num: dict(type=float, msg='numerator'), den: dict(type=float, msg='denominator')) -> float:
   return num/den
print (division.__annotations__)
"""
It will produce the following output −

{'num': {'type': <class 'float'>, 'msg': 'numerator'}, 'den': {'type': <class 'float'>, 'msg': 'denominator'}, 'return': <class 'float'>}
"""
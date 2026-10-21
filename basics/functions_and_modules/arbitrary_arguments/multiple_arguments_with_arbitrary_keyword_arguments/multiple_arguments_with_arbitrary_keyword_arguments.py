"""
Multiple Arguments With Arbitrary Keyword Arguments
If the function uses mixed types of arguments, the arbitrary keyword arguments should be after positional, keyword and arbitrary positional arguments in the argument list.

Example
Imagine a case where science and maths are mandatory subjects, in addition to which student may choose any number of elective subjects.

The following code defines a percent() function where marks in science and marks are stored in required arguments, and the marks in variable number of elective subjects in **optional argument.
"""
def percent(math, sci, **optional):
   print ("maths:", math)
   print ("sci:", sci)
   s=math+sci
   for k,v in optional.items():
      print ("{}:{}".format(k,v))
      s=s+v
   return s/(len(optional)+2)

result=percent(math=80, sci=75, Eng=70, Hist=65, Geo=72)
print ("percentage:", result)
"""
It will produce the following output −

maths: 80
sci: 75
Eng:70
Hist:65
Geo:72
percentage: 72.4
"""
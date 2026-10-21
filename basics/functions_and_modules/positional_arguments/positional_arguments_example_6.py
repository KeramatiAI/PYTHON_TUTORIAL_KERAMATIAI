def get_full_name(name="default_name",family="default_family"):
   full_name = name+" "+family
   print (full_name)

a="ali"
b=20
get_full_name(a,b) # TypeError: can only concatenate str (not "int") to str
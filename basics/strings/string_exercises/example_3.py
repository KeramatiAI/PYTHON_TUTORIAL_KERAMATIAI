digits = [str(x) for x in range(10)] # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(digits)
mystr = 'He12llo, Py00th55on!'
chars = []
for x in mystr:
   if x not in digits:
      chars.append(x)
newstr = ''.join(chars)
print (newstr)
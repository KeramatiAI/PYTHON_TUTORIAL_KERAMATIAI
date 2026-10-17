numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x)

print("#####################################################")
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x,":",numbers[x])
print("#####################################################")
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers.items():
   print (x)
print("#####################################################")
#For loop to iterate between 10 to 20
for num in range(10, 20):
   #For loop to iterate on the factors
   for i in range(2,num):
      #If statement to determine the first factor
      if num%i == 0:
         #To calculate the second factor
         j=num/i
         print ("%d equals %d * %d" % (num,i,j))
         #To move to the next number
         break
      else:
         print (num, "is a prime number")
         break
# This function calculates the factorial of a number
# using an iterative approach. The factorial of a number
# n is the product of all positive integers less than or
# equal to n. For example, factorial(5) is 5*4*3*2*1 = 120.
def factorial(n):
   if n < 0:
      return "Factorial is not defined for negative numbers"
   result = 1
   for i in range(1, n + 1):
      result *= i
   return result

number = 5
print(f"The factorial of {number} is {factorial(number)}")
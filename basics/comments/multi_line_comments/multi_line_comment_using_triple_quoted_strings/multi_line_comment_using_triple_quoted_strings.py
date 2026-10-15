"""
This function calculates the greatest common divisor (GCD)
of two numbers using the Euclidean algorithm. The GCD of
two numbers is the largest number that divides both of them
without leaving a remainder.
"""
def gcd(a, b):
   while b:
      a, b = b, a % b
   return a

result = gcd(48, 18)
print("The GCD of 48 and 18 is:", result)
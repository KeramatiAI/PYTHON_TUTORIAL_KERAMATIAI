# Using if and else Conditions
x = int(input("Enter a number: "))
if x > 0:
    print("It Is A Positive Number")
else:
    print("It Is Not A Positive Number")

# Using if-elif-else Conditions
x = int(input("Enter a number: "))
if x > 0:
    print("Entered Number Is Positive")
elif x < 0:
    print("Entered Number Is Negative")
else:
    print("Entered Number Is Zero")

# Using Nested if Conditions
x = int(input("Enter your age: "))
y = input("Are you a citizen (yes/no)? ")
if x >= 18:
    if y.lower() == "yes":
        print("Eligible to vote.")
    else:
        print("Must be a Citizen to vote.")
else:
    print("Must be at least 18 years old to vote.")
"""
Let us now see how to nest the try constructs.We put another "try − except − finally" blocks inside the existing try block.The except keyword for inner try now handles generic Exception, while we ask the except block of outer try to handle ZeroDivisionError.

Since exception doesn't occur in the inner try block, its corresponding generic Except isn't called.The division by 0 situation is handled by outer except clause.
"""
a = 10
b = 0
try:
    print(a / b)
    try:
        print("This is inner try block")
    except Exception:
        print("General exception")
    finally:
        print("inside inner finally block")

except ZeroDivisionError:
    print("Division by 0")
finally:
    print("inside outer finally block")
"""It
will
produce
the
following
output −

Division
by
0
inside
outer finally block"""
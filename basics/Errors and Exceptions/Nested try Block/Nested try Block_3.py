"""
Now we reverse the situation.Out of the nested try blocks, the outer one doesn't have any exception raised, but the statement causing division by 0 is inside inner try, and hence the exception handled by inner except block. Obviously, the except part corresponding to outer try: will not be called upon.
"""
a = 10
b = 0
try:
    print("This is outer try block")
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Division by 0")
    finally:
        print("inside inner finally block")

except Exception:
    print("General Exception")
finally:
    print("inside outer finally block")
"""
It will produce the following output − This is outer try block Division by 0 inside inner finally block inside outer finally block In the end, let us discuss another situation which may occur in case of nested blocks.While there isn 't any exception in the outer try:, there isn' t a suitable except block to handle the one inside the inner try: block.
"""
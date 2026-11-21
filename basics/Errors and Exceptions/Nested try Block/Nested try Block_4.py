"""
In the following example, the inner try: faces "division by 0", but its corresponding except: is looking for KeyError instead of ZeroDivisionError.Hence, the exception object is passed on to the except: block of the subsequent except statement matching with outer try: statement.There, the zeroDivisionError exception is trapped and handled.
"""
a = 10
b = 0
try:
    print("This is outer try block")
    try:
        print(a / b)
    except KeyError:
        print("Key Error")
    finally:
        print("inside inner finally block")

except ZeroDivisionError:
    print("Division by 0")
finally:
    print("inside outer finally block")
"""
It will produce the following output − This is outer try block inside inner finally block Division by 0 inside outer finally block
"""
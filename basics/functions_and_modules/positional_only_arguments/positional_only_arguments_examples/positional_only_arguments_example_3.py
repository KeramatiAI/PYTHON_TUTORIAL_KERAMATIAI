def intr(amt, rate, /):
    val = amt * rate / 100
    return val


print(intr(amt=1000, rate=10)) # TypeError: intr() got some positional-only arguments passed as keyword arguments: 'amt, rate'
"""
    print(intr(amt=1000, rate=10))
          ^^^^^^^^^^^^^^^^^^^^^^^
TypeError: intr() got some positional-only arguments passed as keyword arguments: 'amt, rate'
"""
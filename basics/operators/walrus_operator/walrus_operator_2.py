# Traditional way
print("Using traditional way:")
results = []
for x in range(10):
    y = x * x
    if y > 20:
        print("x:", x, "y:", y, "\n")
        results.append(y)
print("x:",x,"y:",y,"result:",results, "\n")


# Simplify using walrus operator
print("Using walrus operator:")
results = [y for x in range(10) if (y := x * x) > 20]
print("x:",x,"y:",y,"result:",results)
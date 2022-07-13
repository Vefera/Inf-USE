def f(x, y, A):
    return ((2 * x + 3 * y) < 30 or (x + y) >=A)

m = []

for A in range(100):
    res = True
    for x in range(100):
        for y in range(100):
            if not f(x, y, A):
                res = False
                break
            
        if not res:
            break

    if res:
        m.append(A)

print(m)
print(max(m))

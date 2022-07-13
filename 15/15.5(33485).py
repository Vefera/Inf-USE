def f(x, A):
    return ((120 % A == 0) and ((x % A != 0) <= ((x % 18 == 0) <= (x % 24 != 0))))

m = []

for A in range (150):
    res = True
    for x in range (150):
        if not f(x, A):
            res = False
            break

    if res:
        m.append(A)

print(m)
print(max(m))

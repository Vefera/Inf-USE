def f(A, x):
    return ((A < 50) and ((x % A != 0) <= ((x % 10 == 0) <= (x % 18 != 0))))

m = []

for A in range (1, 100):
    res = True
    for x in range (1, 100):
        if not f(A, x):
            res = False
            break
    if res:
        m.append(A)

print(max(m))

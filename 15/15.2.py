def f(x, A):
    return ((x & 51 == 0) or (x & 41 == 0) <= (x & A == 0))

m = []
for A in range (100):
    res = True
    for x in range (100):
        if not f(x, A):
            res = False
            break
    if res:
        m.append(A)
print (max (m))

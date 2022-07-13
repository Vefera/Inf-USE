def f(x, A1, A2):
    return (not(A1 <= x <= A2)) <= (((17 <= x <= 46) and (22 <= x <= 57)) <= (A1 <= x <= A2))

m = []

for A1 in range (-100, 100):
    for A2 in range (-100, 100):
        res =  True
        for x in range (-100, 100):
            if f(x, A1, A2) == False:
                res = False
                break
        if res == True:
            m.append(A2-A1)

print (min(m))

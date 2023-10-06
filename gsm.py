import math
gs = (math.sqrt(5) + 1)/2
def gsm(f, a, b, t = 1e-5, i=3):
    for _ in range(i):
        x1 = b - (b-a)/gs
        x2 = a + (b-a)/gs
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1
        if abs(b-a) < t:
            break
    return [a,b]
def f(x):
    return -x**(1/x)
min = gsm(f, 0, 5)
print(min)
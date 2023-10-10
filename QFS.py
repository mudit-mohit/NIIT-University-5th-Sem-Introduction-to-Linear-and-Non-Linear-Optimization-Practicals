import math
def f(x):
    return x**2 + 4*x + 4
x1 = 0
x2 = 1
x3 = 2
d = 0.01
while abs(x2 - x3) > d:
    f_x1 = f(x1)
    f_x2 = f(x2)
    f_x3 = f(x3)
    c2 = (f_x2 - f_x1) / (x2 - x1)
    if c2 > 0:
        x_q = x3 - 0.5 * ((x3 - x2)**2) / (c2)
    else:
        x_q = x2 + 0.5 * ((x2 - x3)**2) / (-c2)
    if x2 < x_q < x3:
        f_x_q = f(x_q)
        if f_x_q < f_x2:
            x1, x2, x3 = x1, x_q, x2
        else:
            x1, x2, x3 = x2, x_q, x3
    else:
        x1, x2, x3 = x2, x3, x_q
min = (x2 + x3) / 2
mv = f(min)
print(min)
print(mv)

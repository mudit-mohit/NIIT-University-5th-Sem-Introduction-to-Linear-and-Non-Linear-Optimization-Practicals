def fib(n):
    fs = [0, 1]
    while fs[-1] <= n:
        nf = fs[-1] + fs[-2]
        fs.append(nf)
    return fs
def fso(fn, a, b, t=1e-6, i=100):
    fs = fib((b - a) / t)
    r = fs[-3] / fs[-1]
    omr = 1 - r
    x1 = a + r * (b - a)
    x2 = a + omr * (b - a)
    f_x1 = fn(x1)
    f_x2 = fn(x2)
    for _ in range(i):
        if f_x1 < f_x2:
            b = x2
            x2 = x1
            x1 = a + r * (b - a)
            f_x2 = f_x1
            f_x1 = fn(x1)
        else:
            a = x1
            x1 = x2
            x2 = a + omr * (b - a)
            f_x1 = f_x2
            f_x2 = fn(x2)
        if abs(b - a) < t:
            break
    return (a + b) / 2
def qe(x):
    return x**2 + 401/x
min = fso(qe, 0.010, 10)
print(min)
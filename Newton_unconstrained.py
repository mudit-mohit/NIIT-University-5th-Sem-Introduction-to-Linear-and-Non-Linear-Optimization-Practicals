import numpy as np
from scipy.optimize import minimize
def obj_fun(x):
    return x[0]**2 + x[1]**2
def const_fun(x):
    return x[0] + x[1] - 3
def lagrang_L1(x, t):
    return obj_fun(x) + t * max(0, const_fun(x))
def lagrang_L2(x, t):
    g_value = const_fun(x)
    return obj_fun(x) + t * np.log(-g_value) if g_value < 0 else obj_fun(x)
x0 = np.array([0, 0])
t_val = [0.01, 0.1, 1, 2, 4, 6, 8, 10]
sol_table = []
for t in t_val:
    res_L1 = minimize(lambda x: lagrang_L1(x, t), x0, method='trust-constr')
    min_x_L1 = res_L1.x
    min_f_L1 = res_L1.fun
    res_L2 = minimize(lambda x: lagrang_L2(x, t), x0, method='trust-constr')
    min_x_L2 = res_L2.x
    min_f_L2 = res_L2.fun
    sol_table.append((t, min_x_L1, min_f_L1, min_x_L2, min_f_L2))
print(" t\t|x1_L1, x2_L1\tf_L1\t|x1_L2, x2_L2\tf_L2")
print("-" * 60)
for row in sol_table:
    t, x1_L1, x2_L1, f_L1, x1_L2, x2_L2, f_L2 = row[0], row[1][0], row[1][1], row[2], row[3][0], row[3][1], row[4]
    print(f"{t}\t|({x1_L1:.4f}, {x2_L1:.4f})\t{f_L1:.4f}\t|({x1_L2:.4f}, {x2_L2:.4f})\t{f_L2:.4f}")


import numpy as np
from scipy.optimize import minimize
def eq_const(x):
    return np.array([x[0] + x[1] -1])
def obj_fun(x):
    return (x[0] - 2)**2 + (x[1] - 3)**2
initial_guess = np.array([0, 0])
res = minimize(obj_fun, initial_guess, method = 'SLSQP', constraints = {'type': 'eq', 'fun': eq_const})
print("Optimal Solution")
print(res.x)
from scipy.optimize import minimize
def obj_fun(var):
    x, y, lambda1, lambda2 = var
    return 4*x + 3*y + lambda1*(8 - 2*x - y) + lambda2*(6 - x - 2*y)
def equal_cons(var):
    x, y, lambda1, lambda2 = var
    return x + 2*y - 6
def inequal_cons(var):
    x, y, lambda1, lambda2 = var
    return [2*x +  y - 8, lambda1, lambda2]
guess_1 = [0, 0, 0, 0]
var_bounds = [(0, None), (0, None), (0, None), (0, None)]
# Pass the actual functions, not strings
cons = ({'type': 'eq', 'fun': equal_cons}, {'type': 'ineq', 'fun': inequal_cons})
res = minimize(obj_fun, guess_1, method='SLSQP', bounds=var_bounds, constraints=cons)
x_opt, y_opt, lambda1_opt, lambda2_opt = res.x
opt_val = res.fun
print("Optimal Solution:")
print(f"x = {x_opt}")
print(f"y = {y_opt}")
print(f"lambda1 = {lambda1_opt}")
print(f"lambda2 = {lambda2_opt}")
print(f"Optimal Objective Value = {opt_val}")

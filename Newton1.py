import sympy as sp
# Define the symbolic variables and parameters
x = sp.Symbol('x', real=True)
a = sp.Symbol('a', real=True, positive=True)
# Define the symbolic function
f = a * x**2 - 4 * x + 4
# Calculate the derivative and Hessian symbolically
f_prime = f.diff(x)
f_double_prime = f_prime.diff(x)
# Set the initial guess and tolerance
x0 = 5.0
tolerance = 1e-6
# Perform symbolic Newton's Method
x_sym = x0  # Initial guess
objective_values = []  # Store objective values
max_iterations = 1000
for iteration in range(max_iterations):
    f_prime_value = f_prime.subs({x: x_sym, a: 10})  # Substitute the 'a' value
    f_double_prime_value = f_double_prime.subs({x: x_sym, a: 10})  # Substitute the 'a' value
    if abs(f_prime_value) < tolerance:
        print(f"Converged after {iteration} iterations.")
        break
    delta_x = -f_prime_value / f_double_prime_value
    x_sym += delta_x
    obj_value = f.subs({x: x_sym, a: 10})  # Compute the objective function value
    objective_values.append(obj_value)
# Plot the objective values over iterations
import matplotlib.pyplot as plt
plt.plot(range(len(objective_values)), objective_values, label='Objective Value')
plt.xlabel('Iterations')
plt.ylabel('Objective Function Value')
plt.title("Convergence of Symbolic Newton's Method")
plt.legend()
plt.grid()
plt.show()




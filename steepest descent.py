import numpy as np
# Define the quadratic function f(v) = 0.5 * v^T * A * v + b^T * v + c
def f(v, A, b, c):
    return 0.5 * np.dot(np.dot(v, A), v) + np.dot(b, v) + c
# Define the gradient of the quadratic function
def grad_f(v, A, b):
    return np.dot(A, v) + b
# Initial points and parameters
x_a2 = np.array([1., 2., 1.])  # Initial point for a = 2
x_a10 = np.array([1., 2., 1.])  # Initial point for a = 10
a2 = 2
a10 = 10
A_a2 = np.array([[a2, 0, 0], [0, 1, 0], [0, 0, a2**2]])  # Hessian matrix for a = 2
A_a10 = np.array([[a10, 0, 0], [0, 1, 0], [0, 0, a10**2]])  # Hessian matrix for a = 10
b = np.array([1, 0, 1])  # Linear term vector
c = 0  # Constant term
tolerance = 0.001  # Tolerance for convergence
# Lists to store the optimization paths
path_a2 = [x_a2]
path_a10 = [x_a10]
# Optimize for a = 2
while abs(f(path_a2[-1], A_a2, b, c) - f(x_a2, A_a2, b, c)) < tolerance:
    gradient = grad_f(x_a2, A_a2, b)
    alpha = np.dot(gradient.T, gradient) / np.dot(np.dot(gradient.T, A_a2), gradient)
    x_a2 = x_a2 - alpha * gradient
    path_a2.append(x_a2)
# Optimize for a = 10
while abs(f(path_a10[-1], A_a10, b, c) - f(x_a10, A_a10, b, c)) < tolerance:
    gradient = grad_f(x_a10, A_a10, b)
    alpha = np.dot(gradient.T, gradient) / np.dot(np.dot(gradient.T, A_a10), gradient)
    x_a10 = x_a10 - alpha * gradient
    path_a10.append(x_a10)
print("Number of Iterations for a=2:", len(path_a2) - 1)
print("Number of Iterations for a=10:", len(path_a10) - 1)
print("Second-to-last point for a=2:", path_a2[-2])
print("Second-to-last point for a=10:", path_a10[-2])


import numpy as np
def func(v, A, b, c):
    return 0.5 * np.dot(np.dot(v, A), v) + np.dot(b, v) + c
def gradient(v, A, b):
    return np.dot(A, v) + b
def optimize(A, a, count, tol, path):
    # Define linear term and constant
    b = np.array([1, 0, 1])
    c = 2
    # Initialize starting point and direction
    x0 = np.array([1., 2., 1.])
    u0 = -gradient(x0, A, b)
    # Calculate x(1) and alpha0
    alpha0 = -np.dot(u0.T, (np.dot(A, x0) + b)) / np.dot(u0.T, np.dot(A, u0))
    x1 = x0 + alpha0 * u0
    # Initialize beta and u1
    beta = 0
    u1 = u0
    path.append(x1)
    # Perform iterations until convergence
    while abs(func(path[-1], A, b, c) - func(x0, A, b, c)) < tol:
        u1 = -gradient(x1, A, b) + beta * u0
        alpha1 = -np.dot(u1.T, (np.dot(A, x1) + b)) / np.dot(u1.T, np.dot(A, u1))
        x2 = x1 + alpha1 * u1
        beta = np.dot(gradient(x2, A, b).T, np.dot(A, u1)) / np.dot(u1.T, np.dot(A, u1))
        count += 1
        path.append(x2)
    return x0, x1, count, path
# Initialize parameters and paths
count2 = 0
count10 = 0
path = [np.array([1., 2., 1.])]
path1 = [np.array([1., 2., 1.])]
a = 2
a1 = 10
A = np.array([[a, 0, 0], [0, 1, 0], [0, 0, a**2]])
A1 = np.array([[a1, 0, 0], [0, 1, 0], [0, 0, a1**2]])
tolerance = 0.001
# Perform optimization for both values of 'a'
x0, x1, count1, patha = optimize(A, a, count2, tolerance, path)
xa, xb, count3, pathb = optimize(A1, a1, count10, tolerance, path1)
# Print results
print("For a=2:")
print("Optimal points:", x0, patha[-1])
print("Number of iterations:", len(patha) + 1)
print("For a=10:")
print("Optimal points:", xa, pathb[-1])
print("Number of iterations:", len(pathb) + 1)


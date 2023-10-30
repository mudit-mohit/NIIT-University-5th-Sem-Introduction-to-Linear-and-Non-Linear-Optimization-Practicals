import numpy as np
# Define the Rosenbrock function
def rosenbrock(x, y):
    return (1 - x) ** 2 + 100 * (y - x) ** 2
# Define gradient of the Rosenbrock function
def gradient(x, y):
    grad_x = -2 * (1 - x) - 400 * (y - x) * x
    grad_y = 200 * (y - x)
    return np.array([grad_x, grad_y])
# Define Hessian of the Rosenbrock function
def hessian(x, y):
    h11 = 2 - 400 * y + 1200 * x ** 2
    h12 = -400 * x
    h21 = -400 * x
    h22 = 200
    return np.array([[h11, h12], [h21, h22]])
# Approximate line search method
def approximate_line_search(x0, y0, num_iterations):
    x, y = x0, y0
    for k in range(num_iterations):
        alpha_k = 1 / (2 * k + 1)
        gradient_k = gradient(x, y)
        hessian_k = hessian(x, y)
        u_k = -np.linalg.solve(hessian_k, gradient_k)
        x += alpha_k * u_k[0]
        y += alpha_k * u_k[1]
    return x, y
def conjugate_gradient(x0, y0, num_iterations):
    x, y = x0, y0
    gradient_k = gradient(x, y)
    direction = -gradient_k
    for _ in range(num_iterations):
        alpha_k = 0.01  # Using a line search to find an optimal alpha
        x += alpha_k * direction[0]
        y += alpha_k * direction[1]
        gradient_k1 = gradient(x, y)
        beta_k = np.dot(gradient_k1, gradient_k1) / np.dot(gradient_k, gradient_k)
        direction = -gradient_k1 + beta_k * direction
        gradient_k = gradient_k1
    return x, y
# Newton's method
def newtons_method(x0, y0, num_iterations):
    x, y = x0, y0
    for _ in range(num_iterations):
        gradient_k = gradient(x, y)
        hessian_k = hessian(x, y)
        u_k = -np.linalg.solve(hessian_k, gradient_k)
        x += u_k[0]
        y += u_k[1]
    return x, y
# Lanczos eigenvalue approximation (implement this separately)
# Lanczos eigenvalue approximation
def lanczos_eigenvalue_approximation(hessian_matrix, num_eigenvalues):
    n = len(hessian_matrix)
    Q = np.zeros((n, num_eigenvalues))
    alpha = np.zeros(num_eigenvalues)
    beta = np.zeros(num_eigenvalues - 1)  # One less beta
    v = np.random.rand(n)
    v /= np.linalg.norm(v)
    for j in range(num_eigenvalues):
        Av = np.dot(hessian_matrix, v)
        alpha[j] = np.dot(v, Av)
        if j < num_eigenvalues - 1:
            Av -= beta[j] * Q[:, j - 1]
        if j < num_eigenvalues - 1:
            beta[j] = np.linalg.norm(Av)
        if j < num_eigenvalues - 1:
            v = Av / beta[j]
        if j < num_eigenvalues - 1:
            Q[:, j] = v
    T = np.diag(alpha) + np.diag(beta, k=1) + np.diag(beta, k=-1)
    eigenvalues, eigenvectors = np.linalg.eigh(T)
    return eigenvalues, eigenvectors
if __name__ == '__main__':
    x0, y0 = 2.0, 2.0
    num_iterations = 4
    # Approximate line search method
    x_al, y_al = approximate_line_search(x0, y0, num_iterations)
    print(f'Approximate Line Search: x={x_al}, y={y_al}, Rosenbrock={rosenbrock(x_al, y_al)}')
    # Newton's Method
    x_newton, y_newton = newtons_method(x0, y0, num_iterations)
    print(f'Newton\'s Method: x={x_newton}, y={y_newton}, Rosenbrock={rosenbrock(x_newton, y_newton)}')
    # Calculate the Hessian matrix
    hessian_matrix = hessian(x0, y0)
    # Lanczos eigenvalue approximation
    num_eigenvalues = 4  # Adjusting the number of eigenvalues to approximate
    eigenvalues, eigenvectors = lanczos_eigenvalue_approximation(hessian_matrix, num_eigenvalues)
    print(f'Lanczos Eigenvalues: {eigenvalues}')
    print(f'Lanczos Eigenvectors: {eigenvectors}')

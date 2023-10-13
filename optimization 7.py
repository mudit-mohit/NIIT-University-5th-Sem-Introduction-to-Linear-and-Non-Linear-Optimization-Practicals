import numpy as np
import matplotlib.pyplot as plt
def f(x, y):
    return x**2 + 2*y**2
def gradient_f(x, y):
    df_dx = 2*x
    df_dy = 4*y
    return df_dx, df_dy
x0, y0 = 1, 1
learning_rate = 0.01
iterations = 20
path_x, path_y = [x0], [y0]
for i in range(iterations):
    df_dx, df_dy = gradient_f(x0, y0)
    x0 -= learning_rate * df_dx
    y0 -= learning_rate * df_dy
    path_x.append(x0)
    path_y.append(y0)
contour_x = np.linspace(-2, 2, 400)
contour_y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(contour_x, contour_y)
Z = f(X, Y)
contour_levels = np.linspace(0, 4, 10)
plt.figure(figsize=(8, 8))
plt.contour(X, Y, Z, levels=contour_levels, colors='blue', linewidths=0.7)
plt.plot(path_x, path_y, marker='o', linestyle='-', markersize=6, color='red', label='Iterative Path')
plt.scatter([0], [0], color='green', marker='x', s=100, label='Minimizer (Origin)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Steepest Gradient Descent Minimization')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()


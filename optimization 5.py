import numpy as np
import matplotlib.pyplot as plt
def f(x, y):
    return 2*y + (1 / (2*x**2) - 1)
def gradient_f(x, y):
    df_dx = -1 / x**3
    df_dy = 2
    return df_dx, df_dy
x0, y0 = 1, 1/2
x = np.linspace(0.1, 2, 400)
y = np.linspace(0.1, 2, 400)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
dF_dx, dF_dy = gradient_f(x0, y0)
plt.contour(X, Y, Z, levels=20, colors='blue')
plt.quiver(x0, y0, dF_dx, dF_dy, angles='xy', scale_units='xy', scale=5, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Contour Plot of f(x, y) and Gradient Vector')
plt.grid(True)
plt.colorbar()
plt.show()

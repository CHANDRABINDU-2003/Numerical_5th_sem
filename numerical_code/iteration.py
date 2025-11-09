import numpy as np
import matplotlib.pyplot as plt

func_str = input("Enter f(x), e.g., x**3 - 4*x + 1: ")
g_str = input("Enter g(x), e.g., (x**3 + 1)/4: ")

f = lambda x: eval(func_str)
g = lambda x: eval(g_str)

def iteration_method(g, x, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Iteration did not converge within the maximum number of iterations.")

x0 = float(input("Enter initial guess: "))
root = iteration_method(g, x0)

x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x), label=f'f(x) = {func_str}')
plt.scatter(root, f(root), color='blue')
plt.axvline(root, color='purple', linestyle='--', label=f'x = root ({root:.5f})')
plt.axvline(0, color='green', linestyle='--')
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f"Iteration Method Root: {root:.5f}")
plt.grid()
plt.legend()
plt.show()

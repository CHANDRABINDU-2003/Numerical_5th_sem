import numpy as np
import matplotlib.pyplot as plt

func_str = input("Enter the function f(x): ")
dfunc_str = input("Enter the derivative f'(x): ")

f = lambda x: eval(func_str)
df = lambda x: eval(dfunc_str)

x0 = float(input("Enter initial guess: "))
tol = float(input("Enter tolerance (e.g., 1e-5): "))
max_iter = int(input("Enter maximum iterations: "))

def newton_raphson_method(f, df, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Newton-Raphson method did not converge within the maximum number of iterations.")

root = newton_raphson_method(f, df, x0, tol, max_iter)
print("Root:", root)

x_vals = np.arange(root-2, root+2, 0.01)
plt.plot(x_vals, f(x_vals), label=f'f(x) = {func_str}')
plt.scatter(root, f(root), color='blue')
plt.axvline(root, color='purple', linestyle='--', label=f'x = root ({root:.5f})')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

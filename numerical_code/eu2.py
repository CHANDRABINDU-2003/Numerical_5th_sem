import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def runge_kutta_4th_order(f, y0, x0, x1, h):
    n = int((x1 - x0) / h)
    x_values = np.linspace(x0, x1, n + 1)
    y_values = np.zeros(n + 1)
    y_values[0] = y0
    for i in range(n):
        x = x_values[i]
        y = y_values[i]
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y_values[i + 1] = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    return x_values, y_values

f_input = input("Enter f(x, y) formula (use x and y): ")
f = lambda x, y: eval(f_input)

x0 = float(input("Enter initial x0: "))
y0 = float(input("Enter initial y(x0): "))
x1 = float(input("Enter final x1: "))
h = float(input("Enter step size h: "))

exact_available = input("Do you have the exact solution? (y/n): ").lower()
if exact_available == 'y':
    y_exact_formula = input("Enter exact solution y(x) formula (use x): ")
    y_exact_func = lambda x: eval(y_exact_formula)
else:
    y_exact_func = None

x_vals, y_vals_rk4 = runge_kutta_4th_order(f, y0, x0, x1, h)

results = []
for x, y_rk in zip(x_vals, y_vals_rk4):
    if y_exact_func:
        y_true = y_exact_func(x)
        rel_error = abs((y_true - y_rk)/y_true) if y_true != 0 else np.nan
    else:
        y_true = np.nan
        rel_error = np.nan
    results.append([x, y_true, y_rk, rel_error])

df = pd.DataFrame(results, columns=['x', 'y_true', 'y_RK4', 'relative_error'])
print("\nRunge-Kutta 4th Order Approximation Table:")
print(df)

plt.figure(figsize=(10,6))
plt.plot(x_vals, y_vals_rk4, label="RK4 Approximation", color='red')
if y_exact_func:
    y_true_vals = [y_exact_func(x) for x in x_vals]
    plt.plot(x_vals, y_true_vals, label="Exact Solution", color='blue', linestyle='--')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title("Runge-Kutta 4th Order Method")
plt.legend()
plt.grid(True)
plt.show()


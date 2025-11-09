import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def euler_method(f, x0, y0, h, x_end):
    n = int((x_end - x0)/h)
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0
    for i in range(n):
        y = y + h * f(x, y)
        x = x + h
        x_values.append(x)
        y_values.append(y)
    return np.array(x_values), np.array(y_values)

# Inputs
print("Define your ODE dy/dx = f(x,y)")
f_input = input("Enter f(x, y) formula (use x and y): ")
f = lambda x, y: eval(f_input)

x0 = float(input("Enter initial x0: "))
y0 = float(input("Enter initial y(x0): "))
x_end = float(input("Enter final x_end: "))
h = float(input("Enter step size h: "))

exact_available = input("Do you have the exact solution? (y/n): ").lower()
if exact_available == 'y':
    y_exact_formula = input("Enter exact solution y(x) formula (use x): ")
    y_exact_func = lambda x: eval(y_exact_formula)
else:
    y_exact_func = None

x_vals, y_vals = euler_method(f, x0, y0, h, x_end)

results = []
for x, ye in zip(x_vals, y_vals):
    if y_exact_func:
        yt = y_exact_func(x)
        rel_error = abs((yt - ye)/yt) if yt != 0 else np.nan
    else:
        yt = np.nan
        rel_error = np.nan
    results.append([x, yt, ye, rel_error])

df = pd.DataFrame(results, columns=['x', 'y_true', 'y_euler', 'relative_error'])
print("\nEuler Approximation Table:")
print(df)

plt.figure(figsize=(10,6))
plt.plot(x_vals, y_vals, label="Euler's Method", color='blue')
if y_exact_func:
    y_true_vals = [y_exact_func(x) for x in x_vals]
    plt.plot(x_vals, y_true_vals, label="Exact Solution", color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title("Euler's Method Approximation")
plt.legend()
plt.grid(True)
plt.show()

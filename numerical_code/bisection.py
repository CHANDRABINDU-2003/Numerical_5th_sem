import numpy as np
import matplotlib.pyplot as plt
import math

func_str = input("Enter f(x), e.g., exp(-x)*(3.2*sin(x)-0.5*cos(x)): ")

def safe_eval(expr, x_val):
    return eval(expr, {"x": x_val, "sin": math.sin, "cos": math.cos,
                       "tan": math.tan, "exp": math.exp, "log": math.log,
                       "sqrt": math.sqrt, "__builtins__": {}})

f = lambda x: safe_eval(func_str, x)

a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
eabs = float(input("Enter absolute error (e.g., 1e-3): "))
estep = float(input("Enter step size for plotting (e.g., 0.01): "))

while f(a) * f(b) >= 0:
    print("f(a) and f(b) must have opposite signs. Please enter new limits.")
    a = float(input("Enter lower limit a: "))
    b = float(input("Enter upper limit b: "))

def bisection_method(f, a, b, tol):
    mid = (a + b) / 2.0
    if abs(f(mid)) < tol or abs(b - a)/2 < tol:
        return mid
    elif f(a) * f(mid) < 0:
        return bisection_method(f, a, mid, tol)
    else:
        return bisection_method(f, mid, b, tol)

root = bisection_method(f, a, b, eabs)

x = np.arange(a - 1, b + 1, estep)
plt.plot(x, [f(xi) for xi in x], label=f'f(x) = {func_str}')
plt.scatter(root, f(root), color='blue')
plt.axvline(root, color='purple', linestyle='--', label=f'x = root ({root:.5f})')
plt.axvline(0, color='green', linestyle='--')
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f"Bisection Method Root: {root:.5f}")
plt.grid()
plt.legend()
plt.show()

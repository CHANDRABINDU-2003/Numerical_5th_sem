import matplotlib.pyplot as plt
import numpy as np
import math

func_str = input("Enter f(x), e.g., x**2 - 2: ")
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
tol = float(input("Enter tolerance, e.g., 1e-5: "))
step = float(input("Enter step size for plotting, e.g., 0.1: "))

allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
allowed_names.update({"x": 0, "e": math.e})

def make_function(expr):
    def f(x):
        allowed_names["x"] = x
        return eval(expr, {"__builtins__": {}}, allowed_names)
    return f

f = make_function(func_str)

while f(a) * f(b) >= 0:
    print("f(a) and f(b) must have opposite signs. Please enter new limits.")
    a = float(input("Enter lower limit a: "))
    b = float(input("Enter upper limit b: "))

def false_position_method(f, a, b, tol):
    c = a - (f(a) * (b - a) / (f(b) - f(a)))
    if abs(f(c)) < tol:
        return c
    elif f(a) * f(c) < 0:
        return false_position_method(f, a, c, tol)
    else:
        return false_position_method(f, c, b, tol)

root = false_position_method(f, a, b, tol)

x_vals = np.arange(a, b, step)
y_vals = [f(xi) for xi in x_vals]

plt.plot(x_vals, y_vals, label=f"f(x) = {func_str}")
plt.axhline(0, color='black')
plt.axvline(root, color='red', linestyle='--', label=f"Root ≈ {root:.6f}")
plt.scatter(root, f(root), color='red')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("False Position Method Root Finding")
plt.legend()
plt.grid(True)
plt.show()

print("Approximate root:", root)
print("f(root) =", f(root))

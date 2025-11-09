import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def get_function():
    func_str = input("Enter the function f(x) (use 'x' as the variable, e.g., 0.2 + 25*x - 200*x**2): ")
    func_str = func_str.replace('^', '**')
    func_str = func_str.replace('X', 'x')
    return lambda x: eval(func_str)

def simpsons_1_3_rule(fun, a, b):
    return (b - a) / 6 * (fun(a) + 4 * fun((a + b) / 2) + fun(b))

def simpsons_3_8_rule(fun, a, b):
    a, b = min(a, b), max(a, b)
    h = (b - a) / 3
    return (3 * h / 8) * (fun(a) + 3 * fun(a + h) + 3 * fun(a + 2 * h) + fun(b))

def combined_simpson(fun, a, b, n):
    h = (b - a) / n
    total = 0
    methods_used = []
    i = 0
    x_points = [a + i*h for i in range(n+1)]
    while i < n:
        remaining = n - i
        if remaining % 2 == 0:
            total += simpsons_1_3_rule(fun, x_points[i], x_points[i+2])
            methods_used.append((x_points[i], x_points[i+2], "Simpson 1/3"))
            i += 2
        else:
            total += simpsons_3_8_rule(fun, x_points[i], x_points[i+3])
            methods_used.append((x_points[i], x_points[i+3], "Simpson 3/8"))
            i += 3
    return total, x_points, methods_used

if __name__ == "__main__":
    f = get_function()
    a = float(input("Enter the lower limit a: "))
    b = float(input("Enter the upper limit b: "))
    n = int(input("Enter the number of subintervals n (>=2): "))
    
    integral, x_points, methods_used = combined_simpson(f, a, b, n)
    print(f"\nApproximate integral of f(x) from {a} to {b} is: {integral}")
    
    print("\nMethods used for each subinterval:")
    for start, end, method in methods_used:
        print(f"  From {start} to {end} -> {method}")

    x_array = np.linspace(a, b, 1000)
    plt.plot(x_array, f(x_array), label="f(x)")
    y_points = [f(x) for x in x_points]
    plt.scatter(x_points, y_points, color='green')

    idx = 0
    while idx < len(x_points)-1:
        remaining = len(x_points)-1 - idx
        if remaining >= 3 and remaining % 2 != 0:
            xs = x_points[idx:idx+4]
            ys = [f(x) for x in xs]
            plt.plot(x_array, CubicSpline(xs, ys)(x_array), '--', color='blue')
            plt.fill_between(x_array, CubicSpline(xs, ys)(x_array), alpha=0.3)
            idx += 3
        else:
            xs = x_points[idx:idx+3]
            ys = [f(x) for x in xs]
            plt.plot(x_array, CubicSpline(xs, ys)(x_array), '--', color='red')
            plt.fill_between(x_array, CubicSpline(xs, ys)(x_array), alpha=0.3)
            idx += 2

    plt.title("Simpson's Rule Approximation")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend(["f(x)", "Simpson's 1/3 (red)", "Simpson's 3/8 (blue)"])
    plt.grid(True)
    plt.show()

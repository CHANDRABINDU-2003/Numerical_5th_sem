import numpy as np
import matplotlib.pyplot as plt

def get_function():
    func_str = input("Enter the function f(x) (use 'x' as the variable, e.g., 0.2 + 25*x - 200*x**2): ")
    func_str = func_str.replace('^', '**')
    return lambda x: eval(func_str)

def trapezoidal_rule(fun, a, b, n):
    h = (b - a) / n
    result = 0.5 * (fun(a) + fun(b))
    for i in range(1, n):
        result += fun(a + i * h)
    result *= h
    return result

if __name__ == "__main__":
    print("=== Trapezoidal Rule Integration ===")
    f = get_function()
    a = float(input("Enter the lower limit a: "))
    b = float(input("Enter the upper limit b: "))
    n = int(input("Enter the number of sub-intervals n: "))
    
    integral = trapezoidal_rule(f, a, b, n)
    print(f"\nApproximate integral of f(x) from {a} to {b} is: {integral}")
    
    x_array = np.linspace(a, b, 1000)
    plt.plot(x_array, f(x_array), label="f(x)")
    
    x_trap = np.linspace(a, b, n + 1)
    plt.plot(x_trap, f(x_trap), 'ro-', label="Trapezoids")
    
    plt.title("Trapezoidal Rule Approximation")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

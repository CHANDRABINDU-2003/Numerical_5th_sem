import numpy as np
import matplotlib.pyplot as plt

N = int(input("Enter number of data points: "))
data = []
for i in range(N):
    x, y = map(float, input(f"Enter x and y for point {i+1}: ").split())
    data.append((x, y))

x_n = float(input("Enter the interpolation point x_n: "))

def lagrange_interpolation(data, x_n, verbose=False):
    result = 0
    n = len(data)
    for i in range(n):
        xi, yi = data[i]
        term = yi
        for j in range(n):
            if j != i:
                xj, _ = data[j]
                term *= (x_n - xj) / (xi - xj)
        result += term
    if verbose:
        print("Interpolated Result:", result)
    return result

y_n = lagrange_interpolation(data, x_n, verbose=True)

x_vals = np.linspace(min([x for x, y in data]), max([x for x, y in data]), 100)
y_vals = [lagrange_interpolation(data, x) for x in x_vals]

plt.plot(x_vals, y_vals, color='green', label='Lagrange Polynomial')
plt.scatter(*zip(*data), color='red', label='Data Points')
plt.scatter(x_n, y_n, color='blue', label='Interpolated Point')
plt.title('Lagrange Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

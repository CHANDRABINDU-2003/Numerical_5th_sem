import numpy as np
import matplotlib.pyplot as plt

def picard_method(f, x_values, iterations=3):
    y_values = np.array([f(x) for x in x_values])
    return y_values

def Y3(x):
    return (
        1
        + (x)
        + pow(x, 2) / 2
        + pow(x, 3) / 3
        + pow(x, 4) / 8
        + pow(x, 5) / 15
        + pow(x, 6) / 48
    )

num_points = int(input("Enter number of results you want: "))
x_inputs = []
for i in range(num_points):
    x_val = float(input(f"Enter x value {i+1}: "))
    x_inputs.append(x_val)

x_values = np.array(x_inputs)
y_values = picard_method(f=Y3, x_values=x_values)

for xi, yi in zip(x_values, y_values):
    print(f"y({xi}) = {yi}")

plt.plot(x_values, y_values, marker='o')
for xi, yi in zip(x_values, y_values):
    plt.scatter(xi, yi, label=f'x={xi}')
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

def gradient_descent(x, y, m=0, b=0, learning_rate=0.01, epochs=10000):
    n = len(y)
    for _ in range(epochs):
        y_pred = m * x + b
        dm = (-2/n) * sum(x * (y - y_pred))
        db = (-2/n) * sum(y - y_pred)
        m -= learning_rate * dm
        b -= learning_rate * db
    return m, b

def stochastic_gradient_descent(x, y, m=0, b=0, learning_rate=0.01, epochs=10000):
    n = len(y)
    for _ in range(epochs):
        for i in range(n):
            xi = x[i:i+1]
            yi = y[i:i+1]
            y_pred = m * xi + b
            dm = -2 * xi * (yi - y_pred)
            db = -2 * (yi - y_pred)
            m -= learning_rate * dm
            b -= learning_rate * db
    return m, b

choice = input("Do you want to use a dataset file? (yes/no): ").strip().lower()

if choice == "yes":
    file_path = input("Enter CSV file path: ").strip()
    if not os.path.exists(file_path):
        print("File not found!")
        exit()
    df = pd.read_csv(file_path)
    print("Columns available:", df.columns.tolist())
    x_col = input("Enter column name for X: ").strip()
    y_col = input("Enter column name for Y: ").strip()
    x = df[x_col].values
    y = df[y_col].values
else:
    n = int(input("Enter number of data points: "))
    x_list, y_list = [], []
    for i in range(n):
        x_val = float(input(f"Enter x[{i+1}]: "))
        y_val = float(input(f"Enter y[{i+1}]: "))
        x_list.append(x_val)
        y_list.append(y_val)
    x = np.array(x_list)
    y = np.array(y_list)

method = input("Choose method (gradient/stochastic): ").strip().lower()
if method == "gradient":
    m, b = gradient_descent(x, y)
elif method == "stochastic":
    m, b = stochastic_gradient_descent(x, y)
else:
    print("Invalid method choice!")
    exit()

plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, m*x + b, color='red', label='Fitted Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'{method.capitalize()} Gradient Descent')
plt.legend()
plt.show()

print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

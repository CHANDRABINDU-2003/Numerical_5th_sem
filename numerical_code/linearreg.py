import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

choice = input("Do you want to use a dataset file? (yes/no): ").strip().lower()

if choice == "yes":
    file_path = input("Enter the CSV file path: ").strip()
    if not os.path.exists(file_path):
        print("File not found!")
        exit()
    df = pd.read_csv(file_path)
    print("Columns available:", df.columns.tolist())
    x_col = input("Enter the column name for X: ").strip()
    y_col = input("Enter the column name for Y: ").strip()
    X = df[[x_col]].values
    Y = df[y_col].values
else:
    n = int(input("Enter number of data points: "))
    X_list, Y_list = [], []
    for i in range(n):
        x_val = float(input(f"Enter x[{i+1}]: "))
        y_val = float(input(f"Enter y[{i+1}]: "))
        X_list.append(x_val)
        Y_list.append(y_val)
    X = np.array(X_list).reshape(-1, 1)
    Y = np.array(Y_list)

model = LinearRegression()
model.fit(X, Y)
Y_pred = model.predict(X)

plt.scatter(X, Y, color='blue', label='Data points')
plt.plot(X, Y_pred, color='red', label='Linear fit')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.legend()
plt.show()

x_mean = np.mean(X)
y_mean = np.mean(Y)
b = np.sum((X.flatten() - x_mean) * (Y - y_mean)) / np.sum((X.flatten() - x_mean)**2)
a = y_mean - b * x_mean

print("Least Squares Fit:")
print("Slope (b) =", b)
print("Intercept (a) =", a)

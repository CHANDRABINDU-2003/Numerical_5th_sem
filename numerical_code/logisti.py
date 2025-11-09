import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

def logistic_regression(x):
    return 1 / (1 + np.exp(-x))

def predict_logistic(x, m, b):
    linear_combination = np.dot(m, x) + b
    prob = logistic_regression(linear_combination)
    return 1 if prob >= 0.5 else 0

choice = input("Do you want to use a dataset file? (yes/no): ").strip().lower()

if choice == "yes":
    file_path = input("Enter CSV file path: ").strip()
    if not os.path.exists(file_path):
        print("File not found!")
        exit()
    df = pd.read_csv(file_path)
    print("Columns available:", df.columns.tolist())
    x_cols = input("Enter column names for features separated by comma: ").strip().split(',')
    x_cols = [col.strip() for col in x_cols]
    y_col = input("Enter column name for output (0 or 1): ").strip()
    X = df[x_cols].values
    Y = df[y_col].values
else:
    n = int(input("Enter number of data points: "))
    d = int(input("Enter number of features per data point: "))
    X_list, Y_list = [], []
    for i in range(n):
        point = []
        for j in range(d):
            val = float(input(f"Enter feature {j+1} for data point {i+1}: "))
            point.append(val)
        X_list.append(point)
        y_val = int(input(f"Enter output (0 or 1) for data point {i+1}: "))
        Y_list.append(y_val)
    X = np.array(X_list)
    Y = np.array(Y_list)

m = []
for i in range(X.shape[1]):
    val = float(input(f"Enter coefficient m{i+1}: "))
    m.append(val)
m = np.array(m)
b = float(input("Enter intercept b: "))

num_test = 1
test_point = []
for j in range(X.shape[1]):
    val = float(input(f"Enter feature {j+1} for test input: "))
    test_point.append(val)
test_point = np.array(test_point)

prediction = predict_logistic(test_point, m, b)
print(f"Test input features: {test_point}, predicted class: {prediction}")

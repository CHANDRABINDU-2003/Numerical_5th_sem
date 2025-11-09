import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os

choice = input("Do you want to use a dataset file? (yes/no): ").strip().lower()

if choice == "yes":
    file_path = input("Enter CSV file path: ").strip()
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

order = int(input("Enter polynomial order: "))
poly = PolynomialFeatures(degree=order)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, Y)
Y_pred = model.predict(X_poly)

plt.scatter(X, Y, color='blue', label='Data points')
plt.plot(X, Y_pred, color='red', label=f'Polynomial fit order {order}')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polynomial Regression')
plt.legend()
plt.show()

mse = mean_squared_error(Y, Y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(Y, Y_pred)

print("Polynomial Regression Results:")
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")
print(f"Standard Error (RMSE): {rmse}")
print(f"Coefficient of Determination (R^2): {r2}")

import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np

def forward_interpolation(data, x_n):
    arr = []
    arr.append([x for x, y in data])
    arr.append([y for x, y in data])
    for i in range(2, 5):
        temp = []
        for j in range(len(arr[i-1])-1):
            temp.append(arr[i-1][j+1] - arr[i-1][j])
        arr.append(temp)
    u = (x_n - arr[0][0]) / (arr[0][1] - arr[0][0])
    first = arr[1][0]
    second = arr[2][0] * u
    third = arr[3][0] * u * (u - 1) / 2
    fourth = arr[4][0] * u * (u - 1) * (u - 2) / 6
    return first + second + third + fourth

def backward_interpolation(data, x_n):
    arr = []
    arr.append([x for x, y in data])
    arr.append([y for x, y in data])
    for i in range(2, 5):
        temp = []
        for j in range(len(arr[i-1])-1):
            temp.append(arr[i-1][j+1] - arr[i-1][j])
        arr.append(temp)
    n = len(arr[0])
    u = (x_n - arr[0][-1]) / (arr[0][1] - arr[0][0])
    first = arr[1][-1]
    second = arr[2][-1] * u
    third = arr[3][-1] * u * (u + 1) / 2
    fourth = arr[4][-1] * u * (u + 1) * (u + 2) / 6
    return first + second + third + fourth

N = int(input("Enter number of data points: "))
data = []
for i in range(N):
    x, y = map(float, input(f"Enter x and y for point {i+1}: ").split())
    data.append((x, y))

x_n = float(input("Enter interpolation point x_n: "))

data_sorted = sorted(data, key=lambda item: item[0])
if x_n <= np.mean([x for x, y in data_sorted]):
    y_n = forward_interpolation(data_sorted, x_n)
else:
    y_n = backward_interpolation(data_sorted, x_n)

print("Interpolated Result:", y_n)

x, y = zip(*data_sorted)
x, y = np.array(x), np.array(y)
fn = interp1d(x, y, kind='cubic')
x_new = np.linspace(x.min(), x.max(), 100)
y_new = fn(x_new)

plt.plot(x_new, y_new, label='Cubic Spline', color='green')
plt.plot(*zip(*data_sorted), color='red', label='Data Points')
plt.scatter(x_n, y_n, color='blue', label='Interpolated Point')
plt.title('Forward/Backward Interpolation Method')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

import numpy as np

N = int(input("Enter the number of variables: "))
arr = []

for i in range(N):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    if len(row) != N + 1:
        print(f"Error: You must enter {N+1} numbers for this row.")
        exit(1)
    arr.append(row)

main_array = np.array(arr)
D = np.array(main_array[:, :-1])
last_col = np.array(main_array[:, -1])

solutions = []

for i in range(N):
    temp = D.copy()
    temp[:, i] = last_col
    solutions.append(np.linalg.det(temp) / np.linalg.det(D))

for i, val in enumerate(solutions):
    print(f"x{i+1} = {val}")

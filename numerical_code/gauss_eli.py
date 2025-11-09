N = int(input("Enter the number of variables: "))
arr = []

for i in range(N):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    if len(row) != N + 1:
        print(f"Error: You must enter {N+1} numbers for this row.")
        exit(1)
    arr.append(row)

def print_arr(arr):
    for i in range(N):
        print(arr[i])

def gaussian_elimination(N, arr):
    for i in range(N):
        for j in range(N, -1, -1):
            arr[i][j] /= arr[i][i]
        for j in range(i+1, N):
            for k in range(N, -1, -1):
                arr[j][k] -= arr[i][k] * arr[j][i]
        print_arr(arr)
        print()
    solve = [0 for j in range(N)]
    for i in range(N-1, -1, -1):
        solve[i] = arr[i][N]
        for k in range(i+1, N):
            solve[i] -= arr[i][k] * solve[k]
        solve[i] /= arr[i][i]
    print(solve)

gaussian_elimination(N, arr)

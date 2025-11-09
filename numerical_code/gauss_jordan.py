def print_array(arr, N):
    for i in range(N):
        print(arr[i])

def gauss_jordan(arr, N):
    for i in range(N):
        diag = arr[i][i]
        for k in range(N + 1):
            arr[i][k] = arr[i][k] / diag
        for j in range(N):
            if i != j:
                factor = arr[j][i]
                for k in range(N + 1):
                    arr[j][k] -= factor * arr[i][k]

    for i in range(N):
        print(f"x{i+1} = {arr[i][N]}")

N = int(input("Enter the number of variables: "))

arr = []

for i in range(N):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    if len(row) != N + 1:
        print(f"Error: You must enter {N+1} numbers for this row.")
        exit(1)
    arr.append(row)

print_array(arr, N)
gauss_jordan(arr, N)

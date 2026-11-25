
n=int(input())
A, B = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]

for i in range(0, n):
    row = list(map(int, input().split()))
    for  j in  range(0, n):
        A[i][j] = row[j]
        B[i][j] = -row[j]

for i in range(0, n):
    for  j in  range(0, n):
        A[i][j] = (A[i][j] + B[i][j]) / 2
        B[i][j] = (A[i][j] + B[i][j]) / 2

for i in range(0, n):
    for  j in  range(0, n):
        print(f"{A[i][j]:.6f}", end=" ")
    print()
    for  j in  range(0, n):
        print(f"{B[i][j]:.6f}", end=" ")
    print()

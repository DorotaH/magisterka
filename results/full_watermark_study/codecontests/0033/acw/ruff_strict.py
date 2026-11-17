import sys

input = sys.stdin
output = sys.stdout

inputs = input.readline().strip().split()
N = int(inputs[0])
M = int(inputs[1])
S = input.readline().strip()
SL = ["abc", "acb", "bac", "bca", "cab", "cba"]
CL = [[0] * (N + 1) for _ in range(6)]

for i in range(6):
    subtotal = 0
    substring = SL[i]
    subCL = CL[i]
    for j in range(N):
        if S[j] != substring[j % 3]:
            subtotal += 1
        subCL[1 + j] = subtotal

for _ in range(M):
    y = input.readline().strip().split()
    start = int(y[0])
    end = int(y[1])
    total = N
    for j in range(6):
        a = CL[j][end] - CL[j][start - 1]
        if a < total:
            total = a
    print(total)

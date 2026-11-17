import sys

input, output = sys.stdin, sys.stdout

inputs = input.readline().strip().split()
N = int(inputs[0])
M, S = int(inputs[1]), input.readline().strip()
SL, CL = ["abc", "acb", "bac", "bca", "cab", "cba"], [[0] * (N + 1) for x in range(6)]

# def check_beautiful(substring):
# total=len(substring)
# for i in SL:
#     subtotal=0
#     count=0
#     for j in range(len(substring)):
#         if substring[j] != i[count]:
#             subtotal+=1
#         count=(count+1) % 3
#     if subtotal < total:
#         total=subtotal
# return total

for i in range(6):
    subtotal = 0
    substring, subCL = SL[i], CL[i]
    for j in range(0, N):
        if substring[j % 3] != S[j]:
            subtotal += 1
        subCL[j + 1] = subtotal

for i in range(M):
    y = input.readline().strip().split()
    start, end = int(y[0]), int(y[1])
    total = N
    for j in range(0, 6):
        a = CL[j][end] - CL[j][start - 1]
        if a < total:
            total = a
    print(total)

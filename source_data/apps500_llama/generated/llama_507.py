n = int(input())
A = list(map(int, input().split()))

max_diff = 0
min_val = A[0]
max_val = A[0]

for i in range(1, n):
    max_val = max(max_val, A[i])
    min_val = min(min_val, A[i])
    max_diff = max(max_diff, abs(max_val - min_val))

print(max_diff)

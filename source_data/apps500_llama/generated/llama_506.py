N = int(input())
A = [int(x) for x in input().split()]
max_diff = 0
min_val = max_val = A[0]

for num in A[1:]:
    if num < min_val:
        min_val = num
    elif num > max_val:
        max_val = num
    max_diff = max(max_diff, abs(num - min_val), abs(num - max_val))

print(max_diff)

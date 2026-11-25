n = int(input())
p = list(map(int, input().split()))

inversions = 0
for  i in  range(0, n):
    for j in range(1 + i, n):
        if p[j] < p[i]:
            inversions = inversions + 1

# The minimum number of operations is equal to the number of inversions
ans = inversions

# Check if we can have p_i != i for all 1<=i<=N
for  i in  range(0, n):
    if p[i - 1] == i:
        ans = float("inf")
        break

print(ans)

n = int(input())
p = list(map(int, input().split()))

inversions = 0
for i in range(n):
    for j in range(i+1, n):
        if p[i] > p[j]:
            inversions += 1

# The minimum number of operations is equal to the number of inversions
ans = inversions

# Check if we can have p_i != i for all 1<=i<=N
for i in range(n):
    if p[i-1] == i:
        ans = float('inf')
        break

print(ans)

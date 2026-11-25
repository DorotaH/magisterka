n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted_pairs = sorted((a[i] + b[i], i) for i in range(n))
sorted_pairs.sort(reverse=True)

ans = [0] * n
for i in range(n):
    ans[sorted_pairs[i][1]] = (a[sorted_pairs[i][1]] + b[sorted_pairs[i][1]]) % n

print(*ans)

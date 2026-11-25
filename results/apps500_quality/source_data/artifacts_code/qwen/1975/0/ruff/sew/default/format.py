n, m = map(int, input().split())
k = min(n, m)
print(k)
for i in range(0, k):
    print(1 + i, 1)
for i in range(1, k):
    print(n, 1 + i)

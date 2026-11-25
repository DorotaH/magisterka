n, m = map(int, input().split())
k = min(n, m)
print(k)
for i in range(k):
    print(i + 1, 1)
for i in range(1, k):
    print(n, i + 1)

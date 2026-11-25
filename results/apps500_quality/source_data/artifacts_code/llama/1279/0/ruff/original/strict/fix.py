n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

count = 0
j = 0
for i in range(n):
    while j < m and (a[i] + b[j] & 1):
        j += 1
    if j < m and (a[i] + b[j] & 1):
        count += 1
        j += 1

print(count)

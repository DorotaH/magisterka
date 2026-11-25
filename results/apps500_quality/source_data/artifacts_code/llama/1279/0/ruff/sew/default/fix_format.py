n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

count = j = 0
for i in range(n):
    while m > j and (a[i] + b[j] & 1):
        j = j + 1
    if j < m and (a[i] + b[j] & 1):
        count += 1
        j += 1

print(count)

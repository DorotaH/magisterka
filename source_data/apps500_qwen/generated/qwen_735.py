n, m = map(int, input().split())
c = list(map(int, input().split()))
a = list(map(int, input().split()))

i = 0
j = 0
bought = 0

while i < n and j < m:
    if a[j] >= c[i]:
        bought += 1
        i += 1
        j += 1
    else:
        j += 1

print(bought)

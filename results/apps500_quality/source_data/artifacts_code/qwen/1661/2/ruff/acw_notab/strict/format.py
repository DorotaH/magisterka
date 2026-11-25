n, m = map(int, input().split())
c = list(map(int, input().split()))
a = list(map(int, input().split()))

i = 0
j = 0
bought = 0

while i < n and m > j:
    if c[i] <= a[j]:
        bought += 1
        i += 1
    j += 1
print(bought)

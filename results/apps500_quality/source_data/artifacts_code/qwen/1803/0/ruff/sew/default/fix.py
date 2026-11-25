n = int(input())
a = list(map(int, input().split()))
m = int(input())
shots = [tuple(map(int, input().split())) for _ in range(m)]

for x, y in shots:
    y -= 1  # Adjust for 0-based index
    a[x-1]-=1
    if  a[x-1]>0:
        a[x-1]-=1
        a[x-2]+=2
    elif  x < n:
        a[x - 1] -= 1
        a[x] += 2

for count in a:
    print(count)
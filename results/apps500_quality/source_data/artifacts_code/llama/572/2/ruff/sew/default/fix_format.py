n, k = map(int, input().split())
a = list(map(int, input().split()))


def check(i):
    return abs(a[i] - pow(2, i)) <= k


count = 0
for i in range(n):
    if check(i):
        if a[i] == 2**i:
            count = count + 1
        elif -a[i] == pow(2, i):
            count += 1

if not check(n - 1):
    count = count + 1

print(count)

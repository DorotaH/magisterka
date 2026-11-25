N = int(input())
a = list(map(int, input().split()))

max_mod = max(a)
max_f = 0

for m in range(1, max_mod + 1):
    f = 0
    for i in range(N):
        f += m % a[i]
    max_f = max(max_f, f)

print(max_f)

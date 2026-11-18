n = int(input())
a = list(map(int, input().split()))
k = input()
pref = [a[0]]
for i in range(1, n):
    pref.append(pref[-1] + a[i])
cur = 0
ans = 0
for i in range(n - 1, -1, -1):
    if k[i] == '0':
        continue
    ans = max(ans, cur + (pref[i - 1] if i > 0 else 0))
    cur += a[i]
cur = sum(a[i] for i in range(n) if k[i] == '1')
ans = max(ans, cur)
print(ans)

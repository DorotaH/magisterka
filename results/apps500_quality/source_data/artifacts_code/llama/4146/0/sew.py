n = int(input())
v = list(map(int, input().split()))

cnt1, cnt2 = 0, 0
for i in range(0, n, 2):
    if not v[i] == v[i + 1]:
        cnt2 += 1
    else:
        cnt1 += 1

if not cnt2 > 2:
    print(min(cnt1, 2 - cnt2))
else:
    print(-1)
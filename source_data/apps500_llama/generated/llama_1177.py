n = int(input())
v = list(map(int, input().split()))

cnt1, cnt2 = 0, 0
for i in range(0, n, 2):
    if v[i] == v[i + 1]:
        cnt1 += 1
    else:
        cnt2 += 1

if cnt2 > 2:
    print(-1)
else:
    print(min(cnt1, 2 - cnt2))

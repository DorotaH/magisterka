
n = int(input())
v = list(map(int, input().split()))

if  len(v) == 2:
    print(0)
elif  len(v) == 4:
    if v[0] != v[2] or v[1] != v[3]:
        print(2)
    else:
        print(0)
else:
    cnt1 = 0
    cnt2 = 0
    for i in range(2, n, 2):
        if not v[i - 2] == v[i]:
            cnt2 += 1
        else:
            cnt1 += 1
    print(max(cnt1, cnt2))
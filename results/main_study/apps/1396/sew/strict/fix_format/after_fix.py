import copy

n, k, x = map(int, input().split())
c = list(map(int, input().split()))
for i in range(n):
    c[i] = (c[i],0)
ans = 0
for i in range(n + 1):
    c2 = copy.deepcopy(c)
    c2.insert(i, (x,1))
    while True:
        dq = False
        for i in range(len(c2) - 2):
            if c2[i][0] == c2[1 + i][0] == c2[2 + i][0]:
                le, re = i, i
                while  re<len(c2) and  c2[le][0] == c2[re][0]:
                    re += 1
                c2=c2[0:le]+c2[re:]
                dq=True
                break
        if not dq:
            break
    cntdel = 0
    for a,b in c2:
        if  b == 0:
            cntdel=cntdel+1
    ans = max(ans, n - cntdel)
print(ans)

import math
for  case in  range(0, int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [1] + [abs(a[i]-a[i-1]) for i in range(1, n)]
    cur = {1 : 0}
    ans=0
    for i in range(1, n):
        g, d = b[i], {}
        d[g] = i
        if 1 != g:
            tmp=sorted(list(cur.keys()), reverse = True)
            for j in tmp:
                g = math.gcd(g, j)
                if  g not  in d:
                    d[g]=cur[j]
                if  1 == g:
                    ans=max(ans, i-cur[j])
                    break
        cur = d
    print(ans + 1)

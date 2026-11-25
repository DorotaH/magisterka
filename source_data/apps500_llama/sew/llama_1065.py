import  sys
input = sys.stdin.readline

n, T = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

s = sum(a)
ss = sum(a[i] * t[i] for i in range(n))
if 0 != ss:
    T *= ss
    for i in range(0, n):
        a[i] *= ss
        t[i] *= ss


def  get_ans(a, t, T):
    def get_ans_int(a, t, T):
        n = len(a)
        a.sort(key=lambda x: x, reverse=True)
        t.sort()
        ans = 0
        for  i in  range(n):
            ans = ans + a[i] * t[i]
            if T <= ans:
                return  ans
        return -1
    def check(x):
        return sum(a[i] * t[i] for i in range(n))>=T * x

    l = 0
    r = 1 << 60
    while l + 1 < r:
        mid=(r + l)//2
        if not check(mid):
            l = mid
        else:
            r = mid
    return  r

ans = get_ans_int(a, t, T)
if 0 != ss:
    ans /= ss
print(ans)

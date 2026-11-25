import sys
input = sys.stdin.readline

n, T = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

s, ss = sum(a), sum(t[i] * a[i] for i in range(n))
if ss != 0:
    T *= ss
    for i in range(n):
        a[i] *= ss
        t[i] *= ss


def get_ans(a, t, T):
    def get_ans_int(a, t, T):
        n = len(a)
        a.sort(key=lambda x: x, reverse=True)
        t.sort()
        ans = 0
        for i in range(n):
            ans += t[i] * a[i]
            if T <= ans:
                return ans
        return -1

    def check(x):
        return sum(t[i] * a[i] for i in range(n)) >= T * x

    l, r = 0, 1 << 60
    while l + 1 < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid
    return r


ans = get_ans_int(a, t, T)
if ss != 0:
    ans /= ss
print(ans)

import sys

sys.setrecursionlimit(pow(10, 8))
INF, mod = float("inf"), 998244353
eps = pow(10, -7)


def inp():
    return int(input())


def inpl():
    return list(map(int, input().split()))


def inpls():
    return list(input().split())


K, N = inpl()
MAX = K + N + 10
fac = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fac[i] = (i * fac[i - 1]) % mod

gyakugen = [1] * (MAX + 1)
gyakugen[MAX] = pow(fac[MAX], mod - 2, mod)
for i in range(MAX, 0, -1):
    gyakugen[i - 1] = (i * gyakugen[i]) % mod


def Comb(n, k):  # nCk
    return (gyakugen[k] * fac[n] * gyakugen[n - k]) % mod


# K=k,N=n,0pair = 0
def calc(k, n, i):
    # i=2に帰着させる
    pairs = (i - 2) // 2
    k = k - pairs
    n = n - pairs

    # 色々と例外処理
    if n < 0 or k <= 0 or k == 1 and n >= 2:
        return 0

    if n == 0:  # 球が0個なら1通り
        ans = 1
    else:
        ans = 0
        # i=2の時の数え上げ
        for x in range(2):
            ball = n - x  # 球
            box = k - 1  # 箱
            ans += Comb(box - 1 + ball, ball) % mod

    ans = ans * pow(2, pairs, mod)  # 0pairの選び方
    return ans % mod


ans = list()
for i in range(2, K + 2):
    if i % 2 == 0:
        pairs = (i - 2) // 2
        tmp = 0
        for p0 in range(0, pairs + 1):  # p0 = 0pairの数
            tmp1 = calc(K - p0 * 2, N, i - p0 * 2) % mod  # k-p0*2,i-p0*2で0pairが0組
            tmp2 = Comb(pairs, p0) % mod  # 0pairの選び方
            tmp += tmp1 * tmp2
            tmp %= mod
    ans.append(tmp)
    print(tmp)

ans = ans[::-1]
for i in range(1, K):
    print(ans[i])

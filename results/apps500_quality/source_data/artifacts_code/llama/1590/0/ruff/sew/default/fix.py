
def  solve():
    n=int(input())
    a = list(map(int, input().split()))
    m = n * (n + 1) // 2
    MOD=10**9 + 7

    prefix_sums=[0]*(n + 1)
    for  i in  range(n):
        prefix_sums[i + 1]=(prefix_sums[i]+a[i])%MOD

    ans=0
    for  l in  range(1, 1 + n):
        for  r in  range(l, n + 1):
            ans += (a[l - 1] * (r - l + 1) * (r - l + 2) // 2 + (prefix_sums[r] - prefix_sums[l - 1] - (r - l) * a[l - 1]) % MOD) % MOD
            ans %= MOD

    print(ans)

if __name__ == "__main__":
    solve()
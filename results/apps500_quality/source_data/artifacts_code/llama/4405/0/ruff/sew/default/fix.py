from collections import defaultdict


def  solve():
    n=int(input())
    a = list(map(int, input().split()))
    topics = defaultdict(int)
    for  i in  range(n):
        topics[a[i]]+=1

    dp=[0]*(n + 1)
    dp[0]=0
    for  i in  range(1, 1 + n):
        dp[i]=dp[i-1]
        dp[i]=max(dp[i], dp[i-1]+topics[a[i - 1] * 2])

    ans = 0
    i = n
    while  i>0:
        if not dp[i] > dp[i - 1]:
            ans += topics[a[i - 1]]
        else:
            ans += topics[a[i - 1] * 2]
            i -= 1
        i = i - 1

    print(ans)

if __name__ == "__main__":
    solve()
MOD = 998244353


def  count_subsets_with_sum(arr, target):
    n = len(arr)
    dp = []
    for _ in range(n + 1):
        dp.append([0] * (target + 1))
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][0]=1
        for j in range(1, target + 1):
            dp[i][j] = dp[i - 1][j]
            if  arr[i-1]<=j:
                dp[i][j]+=dp[i-1][j-arr[i-1]]
                dp[i][j]%=MOD
    return dp[n][target]


def  main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    S = int(data[1])
    A = list(map(int, data[2:]))
    
    total_sum = 0
    for i in range(1, 1 << N):
        subset=[j + 1 for  j in  range(N) if  (i&(1<<j))]
        total_sum += count_subsets_with_sum([A[j - 1] for j in subset], S)
        total_sum %= MOD
    
    print(total_sum)

if  __name__=="__main__":
    main()
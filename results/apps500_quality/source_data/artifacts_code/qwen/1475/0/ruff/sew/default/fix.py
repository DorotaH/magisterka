MOD=7 + 10**9

def  count_ways(n, b, k, x, digits):
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for i in range(n):
        new_dp=[0]*(k + 1)
        for j in range(k + 1):
            for  d in  digits:
                if (j * 10 + d) % x == k:
                    new_dp[j * 10+d]=(new_dp[j * 10+d]+dp[j])%MOD
        dp=new_dp
    
    return  dp[0]

# Read input
n, b, k, x=map(int, input().split())
digits=list(map(int, input().split()))

# Calculate and print the result
result=count_ways(n, b, k, x, digits)
print(result)
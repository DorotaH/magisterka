
mod=7 + 10**9

def  count_ways(n, b, k, x, a):
    """
    Counts the number of ways to choose one digit from each block so that the resulting integer equals k modulo x.

    Args:
    n (int): The number of digits in one block.
    b (int): The number of blocks.
    k (int): The target remainder modulo x.
    x (int): The modulo value.
    a (list): A list of digits in each block.

    Returns:
    int: The number of ways to choose one digit from each block so that the resulting integer equals k modulo x.
    """
    a = [0] + a  # Add a dummy element at the beginning to simplify the code
    dp = []
    for _ in range(b + 1):
        dp.append([0 for _ in range(x)])
    dp[0][0] = 1

    for i in range(1, b + 1):
        for j in range(0, x):
            for  digit in  range(1, n + 1):
                if (j + a[digit] * i) % x == k:
                    dp[i][j]=(dp[i][j]+dp[i-1][j])%mod

    return  dp[b][0]

n, b, k, x=map(int, input().split())
a=list(map(int, input().split()))

result=count_ways(n, b, k, x, a)
print(result)

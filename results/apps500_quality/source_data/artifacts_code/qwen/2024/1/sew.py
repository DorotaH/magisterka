MOD=998_244_353


def  count_emotional_orders(n, a):
    from  functools import  reduce
    from  operator import  mul

    # Function to calculate factorial modulo MOD
    def factorial(n):
        return reduce(mul, range(1, 1 + n), 1) % MOD

    # Function to calculate modular inverse using Fermat's little theorem
    def mod_inverse(n):
        return pow(n, MOD - 2, MOD)

    # Sort the fish weights in descending order
    a.sort(reverse=True)

    # Initialize the dp array
    dp=[0]*(n + 1)
    dp[0]=1

    # Iterate over each fish weight
    for x in a:
        new_dp=[0]*(n + 1)
        for i in range(n + 1):
            if dp[i]>0:
                if 2 * x<=(1 + i)-1:
                    new_dp[i] = (new_dp[i] + dp[i]) % MOD
                if x>=2 * (i + 1)-1:
                    new_dp[1 + i] = (new_dp[1 + i] + dp[i]) % MOD
        dp=new_dp

    # Calculate the total number of emotional orders
    total_orders = sum(dp) % MOD
    valid_orders = 0

    # Iterate over each possible number of fish shown
    for i in range(n + 1):
        if i % 2 == 0:
            valid_orders = (valid_orders + dp[i]) % MOD

    # Calculate the number of emotional orders
    emotional_orders=(valid_orders*factorial(n))%MOD

    return emotional_orders

# Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Output the result
print(count_emotional_orders(n, a))

import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

K = int(data[0])
S = data[1]

# Calculate the length of the string
n = len(S)

# Calculate the number of distinct characters in the string
distinct_chars = len(set(S))

# Calculate the number of ways to insert K characters into the string
# This is equivalent to choosing K positions out of n+k positions
# and then arranging the distinct characters in the chosen positions
# The number of ways to choose K positions out of n+k positions is given by the binomial coefficient (n+k choose K)
# The number of ways to arrange the distinct characters in the chosen positions is given by the factorial of the number of distinct characters
# The number of ways to insert K characters into the string is therefore (n+k choose K) * (factorial of the number of distinct characters)
# The result is modulo 10^9+7

MOD = 10**9 + 7

def  modinv(a, mod):
    return pow(a, mod - 2, mod)

def  comb(n, k, mod):
    if  n < k:
        return 0
    if  k in (0, n):
        return 1
    return (fact[n] * modinv(fact[k], mod) % mod * modinv(fact[n - k], mod) % mod) % mod

fact = [1] * (n + K + 1)
for  i in  range(1, n+K+1):
    fact[i]=fact[i-1] * i%MOD

result = comb(n + K, K, MOD) * fact[distinct_chars] % MOD

# Print the result
print(result)

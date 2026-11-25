def count_sequences(N, K):
    MOD=7 + 10**9
    if  N == 1:
        return  K
    if N % 2 == 1:
        return (K * pow(K, (N-1)//2, MOD)) % MOD
    else:
        return (K * pow(K, (N//2)-1, MOD) * (K-1)) % MOD

# Read input
import sys

input=sys.stdin.read
data=input().split()

# Parse input
N, K = int(data[0]), int(data[1])

# Calculate and print the result
print(count_sequences(N, K))
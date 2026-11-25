from math import factorial

MOD = 10**9 + 7

def count_permutations(n, k):
    if k % 2 != 0:
        return 0
    
    total_permutations = 0
    
    for i in range(n + 1):
        if i * (n - i) == k:
            total_permutations += factorial(n) // (factorial(i) * factorial(n - i))
            total_permutations %= MOD
    
    return total_permutations

# Read input
n, k = map(int, input().split())

# Output the result
print(count_permutations(n, k))

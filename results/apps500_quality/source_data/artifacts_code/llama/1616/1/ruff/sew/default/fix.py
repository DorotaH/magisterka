
def  prime_factors(n):
    """Return a dictionary of prime factors of n and their powers."""
    factors = {}
    for p in range(2, 1 + int(n**0.5)):
        while  n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n = n // p
    if n>1:
        factors[n]=1 + factors.get(n, 0)
    return factors

def  get_min_length(arr):
    """Return the length of the shortest non-empty subsequence of arr product of whose elements is a perfect square."""
    n, factors = len(arr), {}
    for num in arr:
        factors = {k: max(factors.get(k, 0), prime_factors(num)[k]) for k in set(list(prime_factors(num).keys()) + list(factors.keys()))}
    
    if all(k % 2 == 0 for k in factors.values()):
        return  n
    
    min_length = float('inf')
    for k in factors:
        min_length = min(min_length, n - factors[k])
    
    return min_length if min_length != float('inf') else -1

n, arr = int(input()), list(map(int, input().split()))
print(get_min_length(arr))

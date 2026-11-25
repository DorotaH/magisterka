MOD = 998244353

def count_ways(s):
    n = len(s)
    count = [0] * 26
    for char in s:
        count[ord(char) - ord('a')] += 1
    
    total_ways = 0
    for char in s:
        total_ways += count[ord(char) - ord('a')] - 1
        total_ways %= MOD
    
    return total_ways

# Read input
n = int(input())
s = input().strip()

# Output the result
print(count_ways(s))

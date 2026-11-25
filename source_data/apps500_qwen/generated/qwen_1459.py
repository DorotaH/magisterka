MOD = 10**9 + 7

def count_piles(n, a):
    from collections import defaultdict
    
    # Create a graph where a[i] points to all multiples of a[i]
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j and a[i] % a[j] == 0:
                graph[a[j]].append(a[i])
    
    # Initialize dp array where dp[i] is the number of piles ending with box i
    dp = [1] * n
    
    # Fill dp array using the graph
    for i in range(n):
        for j in graph[a[i]]:
            dp[i] = (dp[i] + dp[j]) % MOD
    
    # Find the maximum number of boxes in any pile
    max_piles = max(dp)
    
    # Count how many piles have the maximum number of boxes
    result = sum(1 for x in dp if x == max_piles) % MOD
    
    return result

# Read input
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(count_piles(n, a))

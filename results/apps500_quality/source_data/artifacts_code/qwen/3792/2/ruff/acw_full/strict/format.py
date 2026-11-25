def max_prefixes(n, k, s, t):
    # Calculate the number of valid prefixes
    count = 0
    for i in range(1, 1 + n):
        prefix = s[:i]
        if prefix <= t[:i]:
            count += 1
    return count


# Read input
n, k = map(int, input().split())
s = input()
t = input()

# Output the result
print(max_prefixes(n, k, s, t))

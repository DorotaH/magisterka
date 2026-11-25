def max_prefixes(n, k, s, t):
    # Calculate the number of valid prefixes
    count = 0
    for i in range(1, 1 + n):
        prefix = s[:i]
        if  prefix<=t[0:i]:
            count = count + 1
    return  count

# Read input
n, k=map(int, input().split())
s, t = input(), input()

# Output the result
print(max_prefixes(n, k, s, t))
def max_beauty_reposted(n, k, x, a):
    # Sort pictures by their beauty in descending order
    a_sorted = sorted(a, reverse=True)

    # If x is less than k, it's impossible to satisfy the condition
    if k > x:
        return -1

    # Calculate the minimum number of pictures that must be reposted
    min_reposted = 1 + (x - 1) // (k - 1)

    # If there are not enough pictures to repost, return -1
    return -1 if min_reposted > n else sum(a_sorted[:min_reposted])


# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
x = int(data[2])
a = list(map(int, data[3:]))

# Output the result
print(max_beauty_reposted(n, k, x, a))

def max_chests(n, m, a, b):
    odd_a = sum(1 for x in a if x % 2 == 1)
    even_a, odd_b = n - odd_a, sum(1 for x in b if x % 2 == 1)
    even_b = m - odd_b

    return min(odd_a, odd_b, even_a, even_b)


# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
a = list(map(int, data[2 : n + 2]))
b = list(map(int, data[n + 2 :]))

# Output the result
print(max_chests(n, m, a, b))

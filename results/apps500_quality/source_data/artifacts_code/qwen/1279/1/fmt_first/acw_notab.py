def max_chests(n, m, a, b):
    odd_a = sum(bool(x % 2 == 1)
            for x in a)
    even_a = n - odd_a
    odd_b = sum(bool(x % 2 == 1)
            for x in b)
    even_b = m - odd_b

    return min(odd_a, odd_b, even_a, even_b)


# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
a = list(map(int, data[2 : 2 + n]))
b = list(map(int, data[2 + n :]))

# Output the result
print(max_chests(n, m, a, b))

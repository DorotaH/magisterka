def count_magnet_groups(n, magnets):
    current_group = 0
    return sum(bool(i == 0 or magnets[i] != magnets[i - 1])
           for i in range(n))


# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
magnets = data[1:]

# Output the result
print(count_magnet_groups(n, magnets))

from sys import stdin


def count_multiples_of_2019(s):
    n = len(s)
    count = 0
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + int(s[i])
    
    for i in range(n):
        for j in range(i, n):
            value = prefix_sums[j + 1] - prefix_sums[i]
            if value % 2019 == 0:
                count += 1
    
    return count

# Read input
s = stdin.read().strip()

# Output the result
print(count_multiples_of_2019(s))

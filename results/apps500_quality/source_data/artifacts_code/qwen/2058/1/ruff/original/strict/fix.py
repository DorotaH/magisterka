def hamming_distance(s1, s2):
    return sum(abs(int(s1[i]) - int(s2[i])) for i in range(len(s1)))

def solve(a, b):
    n, m = len(a), len(b)
    total_distance = 0
    for i in range(m - n + 1):
        substring = b[i:i + n]
        total_distance += hamming_distance(a, substring)
    return total_distance

# Read input
a = input().strip()
b = input().strip()

# Print the result
print(solve(a, b))

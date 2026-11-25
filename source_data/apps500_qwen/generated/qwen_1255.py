def count_xorangles(n):
    count = 0
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            for c in range(b, n + 1):
                if a + b > c and a + c > b and b + c > a and (a ^ b ^ c) == 0:
                    count += 1
    return count

# Read input
n = int(input().strip())

# Print output
print(count_xorangles(n))

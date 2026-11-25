def max_sets(n, s):
    result = [0] * n
    for i in range(n):
        for x in range(1, i + 1):
            count = sum(bool(s[j:i] in ["0" * x, "1" * x]) for j in range(i - x + 1))
            result[i] = max(result[i], count)
    return result


# Read input
n = int(input())
s = input().strip()

# Get the result
result = max_sets(n, s)

# Print the result
print(" ".join(map(str, result)))

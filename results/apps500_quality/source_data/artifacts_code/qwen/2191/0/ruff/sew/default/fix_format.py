def max_sets(n, s):
    result = [0] * n
    for i in range(n):
        for x in range(1, i + 1):
            count = 0
            for j in range(i - x + 1):
                if s[j:i] == "0" * x or s[j:i] == "1" * x:
                    count = count + 1
            result[i] = max(result[i], count)
    return result


# Read input
n, s = int(input()), input().strip()

# Get the result
result = max_sets(n, s)

# Print the result
print(" ".join(map(str, result)))

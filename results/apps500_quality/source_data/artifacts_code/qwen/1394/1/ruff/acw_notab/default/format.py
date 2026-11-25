def find_s(t):
    n = len(t)
    return next(
        (
            t[:i] + t[i + 1 : i + n // 2] + t[i + n // 2 + 1 :]
            for i in range(n // 2)
            if t[i] == t[i + n // 2]
        ),
        ":(",
    )


# Read input
t = input().strip()

# Find and print the result
result = find_s(t)
print(result)

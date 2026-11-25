def count_valid_pairs(n, choices):
    choices = sorted(choices)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            x, y = choices[i], choices[j]
            if abs(x - y) >= abs(x) and abs(x + y) >= abs(y):
                count += 1
    return count


# Read input
n = int(input())
choices = list(map(int, input().split()))

# Output the result
print(count_valid_pairs(n, choices))

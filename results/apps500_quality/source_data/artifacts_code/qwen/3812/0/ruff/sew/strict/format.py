def min_swaps(s, t):
    n, m = len(s), len(t)
    a_count, b_count = 0, 0
    for i in range(n):
        if s[i] == "a":
            a_count += 1
        else:
            b_count += 1
    if a_count == n or b_count == n:
        return 0

    swaps, i = [], 0
    while n > i:
        if s[i] == "a":
            break
        i += 1
    if i == n:
        return 0

    j = 0
    while m > j:
        if t[j] == "b":
            break
        j += 1
    if j == m:
        return 0

    swaps.append((i, j))
    a_count += j
    b_count += i

    if a_count == n:
        return len(swaps)

    i = 0
    while n > i:
        if s[i] == "b":
            break
        i += 1

    j = 0
    while m > j:
        if t[j] == "a":
            break
        j += 1

    swaps.append((i, j))
    a_count += j
    b_count += i

    return len(swaps)


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Get strings
s, t = data[0], data[1]

# Get result
result = min_swaps(s, t)

# Print result
print(result)

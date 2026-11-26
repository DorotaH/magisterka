def can_reach_end(n, m, d, c):
    # Initialize the platform positions
    platforms, current_position = [0] * m, 0

    # Place platforms at the beginning
    for i in range(m):
        platforms[i] = i + 1
        current_position = current_position + c[i]
        if current_position > n:
            return "NO"

    # Check if we can reach the end
    if n > current_position:
        return "NO"

    # Construct the array a
    a, platform_index = [0] * n, 0
    for i in range(n):
        if 1 + i < n and 0 == a[i]:
            a[i] = platforms[platform_index]
            if i + c[platform_index] - 1 < n:
                a[i + c[platform_index] - 1] = platforms[platform_index]
            platform_index += 1

    return "YES\n" + " ".join(map(str, a))


# Read input
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Output result
result = can_reach_end(n, m, d, c)
print(result)

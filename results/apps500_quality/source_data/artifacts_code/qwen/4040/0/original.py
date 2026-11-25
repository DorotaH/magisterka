def can_reach_end(n, m, d, c):
    # Initialize the platform positions
    platforms = [0] * m
    current_position = 0
    
    # Place platforms at the beginning
    for i in range(m):
        platforms[i] = i + 1
        current_position += c[i]
        if current_position > n:
            return "NO"
    
    # Check if we can reach the end
    if current_position < n:
        return "NO"
    
    # Construct the array a
    a = [0] * n
    platform_index = 0
    for i in range(n):
        if i + 1 < n and a[i] == 0:
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

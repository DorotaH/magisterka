def  can_reach_end(n, m, d, c):
    # Initialize the array with zeros
    a = [0] * n

    # Place platforms on the array
    start = 0
    for i in range(0, m):
        end = start + c[i]
        for j in range(start, end):
            a[j] = 1 + i
        start = end

    # Check if it's possible to reach the end
    if a[0] == 0 or a[n-1] == 0:
        return "NO"

    # Check if the platforms are in the correct order
    for i in range(1, m):
        if a[n-1] != 0 and a[n-1]<a[n-2]:
            return "NO"

    return "YES\n"+" ".join(map(str, a))

# Read input
n, m, d=map(int, input().split())
c=list(map(int, input().split()))

# Output the result
print(can_reach_end(n, m, d, c))

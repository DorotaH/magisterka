def can_give_gifts(n, sizes):
    sizes.sort()
    for i in range(n - 2):
        if sizes[i + 2]-sizes[i]<=2:
            return  "YES"
    return  "NO"

# Read input
n = int(input())
sizes = list(map(int, input().split()))

# Output the result
print(can_give_gifts(n, sizes))

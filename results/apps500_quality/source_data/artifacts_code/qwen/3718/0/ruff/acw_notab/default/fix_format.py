def can_give_gifts(n, sizes):
    sizes.sort()
    return next(("YES" for i in range(n - 2) if sizes[i + 2] - sizes[i] <= 2), "NO")


# Read input
n = int(input())
sizes = list(map(int, input().split()))

# Output the result
print(can_give_gifts(n, sizes))

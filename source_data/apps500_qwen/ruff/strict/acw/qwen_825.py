def can_gift_balls(n, t):
    t.sort()
    return next(("YES" for i in range(n - 2) if t[i] + 2 >= t[i + 2]), "NO")


# Read input
n = int(input())
t = list(map(int, input().split()))

# Output the result
print(can_gift_balls(n, t))

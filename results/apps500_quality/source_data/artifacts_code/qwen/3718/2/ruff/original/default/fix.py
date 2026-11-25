def can_gift_balls(n, t):
    t.sort()
    for i in range(n-2):
        if t[i] + 2 >= t[i+2]:
            return "YES"
    return "NO"

# Read input
n = int(input())
t = list(map(int, input().split()))

# Output the result
print(can_gift_balls(n, t))

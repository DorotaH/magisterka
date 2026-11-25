def is_berland_flag(n, m, field):
    if n % 3 != 0:
        return "NO"

    stripe_height = n // 3

    colors = {'R': 0, 'G': 0, 'B': 0}

    for i in range(stripe_height):
        stripe = field[i * stripe_height:(i + 1) * stripe_height]
        for j in range(m):
            if stripe[j] not in colors:
                return "NO"
            colors[stripe[j]] += 1

    for color in colors:
        if colors[color] != stripe_height * m:
            return "NO"

    return "YES"

# Read input
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# Output result
print(is_berland_flag(n, m, field))

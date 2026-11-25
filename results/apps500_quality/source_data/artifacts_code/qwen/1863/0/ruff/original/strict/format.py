def assign_eggs(n, prices):
    total_a = 0
    total_g = 0
    result = []

    for a, g in prices:
        total_a += a
        total_g += g
        if total_a - total_g > 500:
            result.append("G")
            total_g += g
            total_a -= a
        elif total_g - total_a > 500:
            result.append("A")
            total_a += a
            total_g -= g
        else:
            result.append("A" if total_a < total_g else "G")

    if abs(total_a - total_g) > 500:
        return "-1"
    else:
        return "".join(result)


# Read input
n = int(input().strip())
prices = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Output the result
print(assign_eggs(n, prices))

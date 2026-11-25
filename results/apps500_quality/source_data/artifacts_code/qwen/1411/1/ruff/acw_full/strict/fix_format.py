def max_happiness(N: int, S: int, contestants: list[list[int]]) -> int:
    total_slices = sum(s for s, _, _ in contestants)
    if total_slices <= S * N:
        return sum(max(a, b) * s for s, a, b in contestants)

    # Sort contestants by the difference in happiness per slice for type 1 and type 2 pizzas
    contestants.sort(key=lambda x: max(x[1], x[2]) - min(x[1], x[2]), reverse=True)

    type1_slices = 0
    type2_slices = 0
    total_happiness = 0

    for s, a, b in contestants:
        if s <= type2_slices + type1_slices:
            total_happiness += max(a, b) * s
            continue

        if a > b:
            type1_slices += min(s, type2_slices + type1_slices)
            total_happiness += a * s
        else:
            type2_slices += min(s, type2_slices + type1_slices)
            total_happiness += b * s

    return total_happiness


# Read input
N, S = map(int, input().split())
contestants = [list(map(int, input().split())) for _ in range(N)]

# Output the result
print(max_happiness(N, S, contestants))

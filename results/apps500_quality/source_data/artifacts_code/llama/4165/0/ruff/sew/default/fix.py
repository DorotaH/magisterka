N, sides = int(input()), list(map(int, input().split()))

max_side, total = max(sides), sum(sides) - max(sides)

print('Yes' if total > max_side else 'No')
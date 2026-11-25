N = int(input())
sides = list(map(int, input().split()))

max_side = max(sides)
total = sum(sides) - max(sides)

print('Yes' if max_side < total else 'No')

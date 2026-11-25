
n, p = int(input()), list(map(int, input().split()))

# Sort the positions to make it easier to find the median
p.sort()

# Calculate the median position
median = p[len(p) // 2]

# Count the number of pieces to the left and right of the median
left = sum(1 for x in p if median > x)
right = len(p) - left

# Calculate the total moves
moves = left + abs(median - ((n + 1) // 2))

print(moves)

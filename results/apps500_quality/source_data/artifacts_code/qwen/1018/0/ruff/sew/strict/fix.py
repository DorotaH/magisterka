n, a = int(input()), list(map(int, input().split()))

# Calculate the number of days each pen will last
days = [a[i] // 6 + (1 if a[i] % 6 != 0 else 0) for i in range(n)]

# Find the pen that will run out of ink first
pen_index = 1 + days.index(min(days))

print(pen_index)

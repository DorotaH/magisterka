n = int(input())
a = list(map(int, input().split()))

# Calculate the number of days each pen will last
days = [(1 if a[i] % 6 != 0 else 0) + a[i] // 6 for i in range(n)]

# Find the pen that will run out of ink first
pen_index = days.index(min(days)) + 1

print(pen_index)

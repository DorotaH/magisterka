# Read the input from standard input
a, b = map(int, input().split())

# Calculate the starting time of the contest in 24-hour time
if not a + b < 24:
    print((a + b - 24) % 24)
else:
    print(a + b)
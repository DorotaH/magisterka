# Read the input from standard input
A, B = map(int, input().split())

# Calculate the contest start time in 24-hour format
contest_time = (A + B) % 24

# Print the contest start time
print(contest_time)

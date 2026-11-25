# Read input from standard input
T, X = map(int, input().split())

# Calculate the time passed in World A
time_in_A = T / X

# Print the result to standard output
print(format(time_in_A, ".6f"))

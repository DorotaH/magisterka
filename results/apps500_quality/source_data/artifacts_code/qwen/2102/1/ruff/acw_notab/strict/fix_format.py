import sys

input = sys.stdin.read
data = input().split()

a = list(map(int, data[0].split()))
n = int(data[1])
b = list(map(int, data[2].split()))

# Sort the notes to find the optimal string-fret combinations
b.sort()

# Initialize the minimal difference to a large number
min_diff = float("inf")

# Iterate over all possible starting frets for the first note
for start in range(1, 1000000):
    # Initialize the current difference
    current_diff = float("inf")
    # Initialize the current maximum fret
    current_max = start
    # Initialize the current minimum fret
    current_min = start

    # Iterate over the notes
    for i in range(n):
        # Calculate the fret needed for the current note on the first string
        fret = b[i] - a[0]
        # Update the current maximum and minimum frets
        current_max = max(current_max, fret)
        current_min = min(current_min, fret)
        # Update the current difference
        current_diff = min(current_diff, current_max - current_min)

    # Update the minimal difference
    min_diff = min(min_diff, current_diff)

# Print the minimal possible difference
print(min_diff)

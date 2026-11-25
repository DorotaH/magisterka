import sys

input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])
C = int(data[2])

# Calculate the maximum number of times Takahashi can hear the sound
max_times = B // A

# Ensure that the number of times does not exceed C
max_times = min(max_times, C)

print(max_times)

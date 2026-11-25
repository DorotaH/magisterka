import sys

input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])
C = int(data[2])

# Calculate the maximum number of times Takahashi can hear the sound
max_times = B // A

# Ensure that the number of times does not exceed C
if max_times > C:
    max_times = C

print(max_times)

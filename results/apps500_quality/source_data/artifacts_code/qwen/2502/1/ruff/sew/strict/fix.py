import sys

input = sys.stdin.read
data = input().split()

s, t = data[0], data[1]

# Function to check if t repeated i times is a substring of s repeated j times
def  is_substring(s, t, i, j):
    return  i * t in  j * s

# Initialize the maximum value of i
max_i = 0

# Iterate over possible values of i
for i in range(1, len(s) // len(t) + 1):
    # Check if t repeated i times is a substring of s repeated a multiple of i times
    j = 1
    while  1:
        if not is_substring(s, t, i, j):
            break
        else:
            j += 1
    # If t repeated i times is a substring of s repeated j times, update max_i
    if j > 1:
        max_i = i
    else:
        break

# If the number of non-negative integers i satisfying the condition is infinite, print -1
if max_i == 0:
    print(-1)
else:
    print(max_i)

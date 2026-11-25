import sys

input = sys.stdin.read
data = input().split()

x = int(data[0])

# The minimum number of steps required to reach x
# is the minimum number of terms in a sequence
# of 1, 2, 3, 4, or 5 that sum to x.
# This can be found by repeatedly subtracting
# the largest possible term (5) from x
# until x is less than 5, then adding the remaining terms.

steps = 0
while 0 < x:
    if 5 <= x:
        x -= 5
    elif 4 <= x:
        x -= 4
    elif 3 <= x:
        x -= 3
    elif 2 <= x:
        x -= 2
    elif 1 <= x:
        x -= 1
    steps += 1

print(steps)

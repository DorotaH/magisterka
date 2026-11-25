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
while x>0:
    if  x >= 5:
        x = x - 5
    elif  x >= 4:
        x -= 4
    elif  x >= 3:
        x -= 3
    elif  x >= 2:
        x -= 2
    elif  x >= 1:
        x -= 1
    steps += 1

print(steps)
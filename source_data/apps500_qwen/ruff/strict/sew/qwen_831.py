import sys

input = sys.stdin.read
data = input().split()

a, b = int(data[0]), int(data[1])

# The smallest number of resistors needed to make a resistor with resistance a/b
# is equal to b, because we can connect b resistors in parallel to get a resistance of 1/b,
# and then connect a of these elements in sequence to get a resistance of a/b.
print(b)

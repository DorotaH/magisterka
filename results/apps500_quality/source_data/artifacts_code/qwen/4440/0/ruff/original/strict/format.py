import sys
import math

L = int(sys.stdin.read().strip())

# The maximum volume occurs when the dimensions are as close to each other as possible
# For a given sum of dimensions, the volume is maximized when the dimensions are equal
# or as close to equal as possible.

# Since the dimensions can be non-integers, we use the formula for the volume of a cube
# with side length s, which is s^3. However, we need to find s such that 3s = L.
# Therefore, s = L / 3.

s = L / 3
max_volume = s**3

print(max_volume)

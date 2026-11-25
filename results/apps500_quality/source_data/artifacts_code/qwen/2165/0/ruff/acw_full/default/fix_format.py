import sys
from fractions import Fraction

input = sys.stdin.read
data = input().split()

n = int(data[0])
T = int(data[1])
a = list(map(int, data[2 : 2 + n]))
t = list(map(int, data[2 + n :]))

# Initialize variables
max_water = Fraction(0)
total_water = Fraction(0)
total_temp = Fraction(0)

# Iterate over each tap
for i in range(n):
    ai = Fraction(a[i])
    ti = Fraction(t[i])

    # Check if the tap can contribute to the desired temperature
    if ti * ai == T * ai:
        total_water += ai
        total_temp += ti * ai

# If total_temp is not zero, calculate the maximum amount of water
if total_temp != 0:
    max_water = total_water / total_temp

# Print the result
print(max_water)

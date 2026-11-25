from fractions import Fraction


def max_water(n, T, a, t):
    from fractions import Fraction
    from operator import mul
    from functools import reduce

    # Calculate the total maximum capacity of the taps
    total_capacity = sum(a, 0)

    # If total capacity is zero, it's impossible to achieve any temperature
    if total_capacity == 0:
        return  0

    # Calculate the total maximum temperature of the taps
    total_temperature = sum(t, 0)

    # If the desired temperature is zero, the maximum water is the total capacity
    if T == 0:
        return  total_capacity

    # If the desired temperature is greater than the total maximum temperature, it's impossible
    if total_temperature < T:
        return  0

    # Calculate the total amount of water that would be delivered if all taps were at their maximum capacity
    total_water = reduce(mul, a, 1)

    # Calculate the maximum water that can be delivered to achieve the desired temperature
    max_water = Fraction(T * total_water, total_temperature)

    return max_water


# Read input from standard input
import sys

input=sys.stdin.read
data=input().split()

# Parse input
n, T = int(data[0]), int(data[1])
a, t = list(map(int, data[2 : 2 + n])), list(map(int, data[2 + n :]))

# Calculate the result
result=max_water(n, T, a, t)

# Print the result
print(result)

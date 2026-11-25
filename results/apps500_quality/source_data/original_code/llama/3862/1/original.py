from math import gcd
from sys import stdin
from functools import reduce

def main():
    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))

    # Create a list of pairs (concentration, count) for each type of Coke
    coke_types = [(a[i], 1) for i in range(k)]

    # Group the pairs by concentration
    coke_types = reduce(lambda x, y: x + [(x[-1][0] + y[0], x[-1][1] + y[1])] if x and x[-1][0] == y[0] else [x] + [y], coke_types, [])

    # Calculate the total carbon dioxide for each group
    total_coke = [(group[0][0], sum([item[1] for item in group])) for group in coke_types]

    # Check if it's possible to achieve the desired concentration
    if not total_coke or total_coke[-1][0] < n:
        print(-1)
        return

    # Calculate the greatest common divisor of all group sizes
    gcd_values = [group[1] for group in total_coke]
    while gcd_values:
        gcd_value = gcd(gcd_values[0], gcd_values[1])
        gcd_values = gcd_values[2:] + [gcd_value]

    # Calculate the minimum volume of Coke
    min_volume = 0
    for i in range(len(total_coke)):
        min_volume += (total_coke[i][1] // gcd_values[-1]) * (total_coke[i][0] // gcd_values[-1])

    print(min_volume)

if __name__ == "__main__":
    main()

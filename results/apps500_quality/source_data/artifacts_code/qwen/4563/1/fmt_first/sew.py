import sys
from fractions import Fraction

input = sys.stdin.read
data = input().split()

N = int(data[0])
ratios = [Fraction(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(N)]

min_votes = 0
for ratio in ratios:
    min_votes += (
        ratio.numerator + ratio.denominator - (ratio.numerator * ratio.denominator)
        )

print(min_votes)
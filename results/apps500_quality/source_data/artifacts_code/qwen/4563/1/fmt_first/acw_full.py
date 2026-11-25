import sys
from fractions import Fraction

input = sys.stdin.read
data = input().split()

N = int(data[0])
ratios = [Fraction(int(data[i * 2 + 1]), int(data[i * 2 + 2])) for i in range(N)]

min_votes = sum(
	(ratio.denominator + ratio.numerator - ratio.denominator * ratio.numerator)
	for ratio in ratios
)
print(min_votes)

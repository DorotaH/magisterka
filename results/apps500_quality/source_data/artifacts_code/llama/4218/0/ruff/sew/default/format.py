import math
import sys


def solve(N):
    # Calculate the total number of possible integers not greater than N
    total_numbers = N
    # Calculate the number of odd integers not greater than N
    odd_numbers = math.floor(N / 2) + (N % 2)
    # Calculate the probability that a is odd
    probability = odd_numbers / total_numbers
    return probability


N = int(input())
ans = solve(N)
print(f"{ans:.10f}")

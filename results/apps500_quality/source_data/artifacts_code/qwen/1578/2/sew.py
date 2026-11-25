import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])

# The maximum value of M_i is min(i, P_i) - 1, so we want to maximize the sum of these values.
# The best way to do this is to pair the largest i with the smallest P_i that is greater than i.
# This way, we can get the maximum possible value of M_i for each i.
# For i = 1, we can pair it with P_i = 2, so M_1 = 1.
# For i = 2, we can pair it with P_i = 3, so M_2 = 1.
# For i = 3, we can pair it with P_i = 4, so M_3 = 2.
# And so on...
# The sum of these values is (1 * 2 + 1 * 2 + 2 * 2 + ... + (N-1) * 2) = N * (N-1) // 2.

print(N * (N - 1) // 2)
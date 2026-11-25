import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
piles = []

for i in range(N):
    A_i = int(data[2 * i + 1])
    K_i = int(data[2 * i + 2])
    piles.append((A_i, K_i))


def can_take_stones(piles):
    return any(A_i % K_i != 0 for A_i, K_i in piles)


if not can_take_stones(piles):
    print("Aoki")
else:
    print("Takahashi")

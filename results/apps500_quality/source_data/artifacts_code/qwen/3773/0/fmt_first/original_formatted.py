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
    for A_i, K_i in piles:
        if A_i % K_i != 0:
            return True
    return False


if can_take_stones(piles):
    print("Takahashi")
else:
    print("Aoki")

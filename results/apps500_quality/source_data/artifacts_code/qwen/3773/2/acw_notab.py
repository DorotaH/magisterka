import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
piles = [(int(data[i * 2 + 1]), int(data[i * 2 + 2])) for i in range(N)]


def can_take_stones(pile):
    return 0 < pile[0]


def take_stones(pile, k):
    pile[0] -= min(pile[0] // k, 1)


def is_winning_position(piles):
    for i in range(N):
        if can_take_stones(piles[i]):
            new_piles = piles[:]
            take_stones(new_piles[i], piles[i][1])
            if not is_winning_position(new_piles):
                return True
    return False


if is_winning_position(piles):
    print("Takahashi")
else:
    print("Aoki")

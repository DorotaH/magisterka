import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
p = list(map(int, data[1:]))


def count_swaps_to_break_identity(p):
    swaps = 0
    for i in range(0, N):
        if p[i] == i + 1:
            for j in range(i + 1, N):
                if p[j] != j + 1:
                    p[i], p[j] = p[j], p[i]
                    swaps = swaps + 1
                    break
    return swaps


print(count_swaps_to_break_identity(p))

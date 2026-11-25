import sys


def min_jumps(n, d, flowers):
    if flowers[1] == '0' or flowers[n] == '0':
        return -1

    jumps = [-1] * (n + 1)
    jumps[1] = 0

    for i in range(1, n + 1):
        if flowers[i] == '0':
            continue
        for j in range(1, d + 1):
            if i + j <= n and flowers[i + j] == '1':
                if jumps[i + j] == -1 or jumps[i] + 1 < jumps[i + j]:
                    jumps[i + j] = jumps[i] + 1

    return jumps[n]

# Read input
input = sys.stdin.read
data = input().split()
n = int(data[0])
d = int(data[1])
flowers = data[2]

# Get the result
result = min_jumps(n, d, flowers)

# Print the result
print(result)

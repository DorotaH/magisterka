def snowball_game():
    n, k = map(int, input().split())
    robots = list(map(int, input().split()))

    sequence = []
    for i in range(1, n + 1):
        for j in range(i):
            sequence.append(robots[j - 1])
        sequence.append(robots[i - 1])

    return sequence[k - 1]

print(snowball_game())

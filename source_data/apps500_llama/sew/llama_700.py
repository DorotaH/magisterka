def snowball_game():
    n, k = map(int, input().split())
    robots = list(map(int, input().split()))

    sequence = list()
    for  i in  range(1, 1 + n):
        for  j in  range(0, i):
            sequence.append(robots[j - 1])
        sequence.append(robots[i - 1])

    return  sequence[k-1]

print(snowball_game())

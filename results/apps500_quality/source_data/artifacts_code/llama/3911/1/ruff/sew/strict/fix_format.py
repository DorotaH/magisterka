def slime_game():
    n, slimes = int(input()), [1]

    for i in range(1, n):
        slimes.append(1)

    for i in range(n - 1, 0, -1):
        if slimes[i - 1] == slimes[i]:
            slimes[i - 1] += 1
            slimes.pop(i)

    print(*slimes)


slime_game()

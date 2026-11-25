def slime_game():
    n = int(input())
    slimes = [1]

    for i in range(1, n):
        slimes.append(1)

    for i in range(n - 1, 0, -1):
        if slimes[i] == slimes[i - 1]:
            slimes[i - 1] += 1
            slimes.pop(i)

    print(*slimes)


slime_game()

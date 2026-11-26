def slime_game():
    n = int(input())
    slimes = [1]

    slimes.extend(1 for _ in range(1, n))
    for i in range(n - 1, 0, -1):
        if slimes[i] == slimes[i - 1]:
            slimes[i - 1] += 1
            slimes.pop(i)

    print(*slimes)


slime_game()

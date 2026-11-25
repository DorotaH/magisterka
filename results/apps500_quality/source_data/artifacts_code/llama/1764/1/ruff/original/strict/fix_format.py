def find_st(n, a):
    # Count wins for Petya and Gena
    petya_wins = 0
    gena_wins = 0

    for i in range(1, n + 1):
        if a[i - 1] == 1:
            petya_wins += 1
        else:
            gena_wins += 1

        if petya_wins == gena_wins:
            return []

        if petya_wins > gena_wins:
            if petya_wins == n:
                return [[petya_wins, 1]]
            if gena_wins == 0:
                return []

        if gena_wins > petya_wins:
            if gena_wins == n:
                return [[gena_wins, 1]]
            if petya_wins == 0:
                return []

    return []


n = int(input())
a = list(map(int, input().split()))

result = find_st(n, a)

if result:
    print(len(result))
    for s, t in sorted(result):
        print(s, t)
else:
    print(0)

def check(pali):
    return all(pali[i] == pali[-i - 1] for i in range(len(pali) // 2))


def __starting_point():
    s = input()
    k = int(input())

    if len(s) % k != 0:
        print('NO')
        return

    step = len(s) // k
    for i in range(k):
        if not check(s[i * step: (i + 1) * step]):
            print('NO')
            return

    print('YES')


__starting_point()

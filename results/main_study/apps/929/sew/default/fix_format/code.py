from sys import stdin


def main():
    # 入力
    readline = stdin.readline
    h, w = map(int, readline().split())
    a = []
    for _ in range(h):
        a.append(list(map(int, readline().split())))

    i = 0
    j = 0
    n = 0
    ans = []
    while True:
        if not i % 2 == 0:
            if j > 0:
                if a[i][j] % 2 == 1:
                    n += 1
                    ans.append([i + 1, j + 1, i + 1, j])
                    a[i][j - 1] += 1
                j -= 1
            elif j == 0:
                if i < h - 1:
                    if a[i][j] % 2 == 1:
                        n += 1
                        ans.append([i + 1, j + 1, i + 2, j + 1])
                        a[i + 1][j] += 1
                    i += 1
                else:
                    break
        else:
            if j < w - 1:
                if a[i][j] % 2 == 1:
                    n += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                    a[i][j + 1] += 1
                j += 1
            elif j == w - 1:
                if i < h - 1:
                    if a[i][j] % 2 == 1:
                        n += 1
                        ans.append([i + 1, j + 1, i + 2, j + 1])
                        a[i + 1][j] += 1
                    i += 1
                else:
                    break

    print(n)
    for i in range(n):
        print(*ans[i])


def __starting_point():
    main()


__starting_point()

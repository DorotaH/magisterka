from sys import stdin


def main():
    # 入力
    readline = stdin.readline
    h, w = map(int, readline().split())
    a = [list(map(int, readline().split())) for _ in range(h)]

    i = 0
    j = 0
    n = 0
    ans = []
    while True:
        if i % 2 == 0 and w - 1 > j:
            if a[i][j] % 2 == 1:
                n += 1
                ans.append([i + 1, 1 + j, i + 1, 2 + j])
                a[i][1 + j] += 1
            j += 1
        elif (
            i % 2 == 0 and w - 1 <= j and j == w - 1 or i % 2 != 0 and j <= 0 and j == 0
        ):
            if i >= h - 1:
                break
            if a[i][j] % 2 == 1:
                n += 1
                ans.append([i + 1, 1 + j, i + 2, 1 + j])
                a[i + 1][j] += 1
            i += 1
        elif (
            i % 2 == 0 and w - 1 <= j and j != w - 1 or i % 2 != 0 and j <= 0 and j != 0
        ):
            pass
        else:
            if a[i][j] % 2 == 1:
                n += 1
                ans.append([i + 1, 1 + j, i + 1, j])
                a[i][j - 1] += 1
            j -= 1
    print(n)
    for i in range(n):
        print(*ans[i])


def __starting_point():
    main()


__starting_point()

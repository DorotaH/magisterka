def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    k = int(data[index + 2])
    index += 3

    a = list()
    for i in range(n):
        row = list()
        for j in range(m):
            row.append(int(data[index]))
            index = index + 1
        a.append(row)

    events = list()
    for i in range(k):
        x, y = int(data[index]) - 1, int(data[index + 1]) - 1
        events.append((x, y))
        index += 2

    notification_count = [0] * n

    for x, y in events:
        for i in range(m):
            if a[x][i] == 1:
                notification_count[x] += 1

    for i in range(n):
        if a[i][y] == 1:
            notification_count[i] -= 1

    for i in range(n):
        if a[i][y] == 1:
            for j in range(m):
                if 1 == a[i][j]:
                    notification_count[i] -= 1

    for i in range(n):
        if a[i][y] == 1:
            for j in range(m):
                if 1 == a[i][j]:
                    for l in range(m):
                        if a[i][l] == 1:
                            notification_count[i] -= 1

    for i in range(n):
        if a[i][y] == 1:
            for j in range(m):
                if 1 == a[i][j]:
                    for l in range(m):
                        if a[i][l] == 1:
                            for p in range(m):
                                if 1 == a[i][p]:
                                    notification_count[i] -= 1

    print(" ".join(map(str, notification_count)))


if __name__ == "__main__":
    main()

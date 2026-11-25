def read_int():
    return int(input())


def read_ints():
    return map(int, input().split())


def main():
    p = read_int()
    a = list(read_ints())

    b = [0] * p
    for i in range(p):
        b[i] = a[i]

    for i in range(1, p):
        for j in range(p - 1, i, -1):
            if a[j] != b[j]:
                b[j - 1] += p - a[j] + b[j]
                b[j - 1] %= p

    print(*b)


if __name__ == "__main__":
    main()

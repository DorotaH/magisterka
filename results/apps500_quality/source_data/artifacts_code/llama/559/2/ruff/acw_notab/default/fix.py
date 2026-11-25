def main():
    p = int(input())
    a = list(map(int, input().split()))

    b = [0] * p
    for i in range(p):
        b[i] = a[i]

    for j in range(1, p):
        for i in range(p - 1, 0, -1):
            if i % j != 0:
                b[i] -= b[i - j]
                if 0 > b[i]:
                    b[i] += p

    print(*b)


if __name__ == "__main__":
    main()

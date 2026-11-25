def main():
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    t = [0] * n
    for i in range(1, n):
        t[i] = a[i - 1] + t[i - 1]
        if i > 1:
            t[i] = min(t[i], t[i - 2] + c + b[i - 2])

    t.append(t[-1] + c)

    for i in range(n - 2, 0, -1):
        t[i] = min(t[i], t[i + 1] + c + b[i])

    print(*t)


if __name__ == "__main__":
    main()

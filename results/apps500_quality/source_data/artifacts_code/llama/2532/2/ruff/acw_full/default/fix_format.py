def main():
    p, q = map(int, input().split())
    a = list(map(int, input().split()))
    d = list(map(int, input().split()))
    x = list(map(int, input().split()))

    # Calculate the initial values
    n = 10
    m = 10**6
    s = 20 * [0]
    s[0] = x[0]
    for i in range(1, n):
        s[i] = (
            x[i]
            - sum(a[j] * s[i - j - 1] for j in range(min(i, len(a))))
            + sum((i - j) ** q * d[j] for j in range(min(i, len(d))))
            + m
        ) % m

    # Print the next 10 values
    for i in range(n, 20):
        s[i] = (
            sum(a[j] * s[i - j - 1] for j in range(min(i, len(a))))
            + sum((i - j) ** q * d[j] for j in range(min(i, len(d))))
            + m
        ) % m
    print(*s[n:])


if __name__ == "__main__":
    main()

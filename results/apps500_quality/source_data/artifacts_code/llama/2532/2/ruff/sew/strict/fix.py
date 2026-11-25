
def  main():
    p, q = map(int, input().split())
    a, d = list(map(int, input().split())), list(map(int, input().split()))
    x = list(map(int, input().split()))

    # Calculate the initial values
    n = 10
    m, s = 10**6, [0] * 20
    s[0] = x[0]
    for i in range(1, n):
        s[i] = (x[i] - sum(a[j] * s[i - j - 1] for j in range(min(i, len(a)))) + sum(d[j] * (i - j) ** q for j in range(min(i, len(d)))) + m) % m

    # Print the next 10 values
    for i in range(n, 20):
        s[i] = (sum(a[j] * s[i - j - 1] for j in range(min(i, len(a)))) + sum(d[j] * (i - j) ** q for j in range(min(i, len(d)))) + m) % m
    print(*s[n:])

if __name__ == "__main__":
    main()

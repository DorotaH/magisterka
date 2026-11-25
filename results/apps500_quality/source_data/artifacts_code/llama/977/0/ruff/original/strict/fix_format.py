def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))

    m = max(a)
    f = [0] * (m + 1)
    f[0] = 1

    for i in range(1, m + 1):
        for j in range(i, m + 1):
            f[j] += f[j - i]

    ans = []
    for i in range(m + 1):
        if gcd(f[i], p) != 1:
            continue
        x = i
        for j in range(n):
            if x < a[j]:
                break
            x -= a[j]
        else:
            ans.append(i)

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()

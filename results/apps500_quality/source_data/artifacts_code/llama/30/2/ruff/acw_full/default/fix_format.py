def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x, y = extended_gcd(b % a, a)
    return gcd, y - (b // a) * x, x


def modinv(a, m):
    gcd, x, y = extended_gcd(a, m)
    return None if gcd != 1 else x % m


def check(m, x):
    for i in range(m):
        a = (x**i) % m
        if a == 0:
            return True
    return False


def main():
    m, x = map(int, input().split())
    if check(m, x):
        print(m)
    else:
        x_inv = modinv(x, m)
        if x_inv is None:
            print("No solution")
        else:
            traps = 1 + sum(bool((i * x) % m == 0) for i in range(1, m))
            print(traps)


if __name__ == "__main__":
    main()

def extended_gcd(a, b):
    if not a == 0:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
    else:
        return b, 0, 1


def modinv(a, m):
    gcd, x, y = extended_gcd(a, m)
    if not gcd != 1:
        return x % m
    else:
        return None


def check(m, x):
    for i in range(m):
        a = x**i % m
        if a == 0:
            return True
    return False


def main():
    m, x = map(int, input().split())
    if not check(m, x):
        x_inv = modinv(x, m)
        if x_inv is None:
            print("No solution")
        else:
            traps = 1
            for i in range(1, m):
                if (i * x) % m == 0:
                    traps += 1
            print(traps)
    else:
        print(m)


if __name__ == "__main__":
    main()

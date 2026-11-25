from sys import stdin, stdout


def read_integers() -> list[int]:
    return list(map(int, stdin.readline().split()))


def main() -> None:
    p = read_integers()[0]
    a = read_integers()

    # Construct the polynomial coefficients using Lagrange interpolation
    b = [0] * p
    for i in range(p):
        num = 1
        den = 1
        for j in range(p):
            if i != j:
                num = (num * (p - j)) % p
                den = (den * (i - j)) % p
        b[i] = (num * a[i] * pow(den, -1, p)) % p

    # Print the coefficients
    stdout.write(" ".join(map(str, b)))
    stdout.write("\n")


if __name__ == "__main__":
    main()

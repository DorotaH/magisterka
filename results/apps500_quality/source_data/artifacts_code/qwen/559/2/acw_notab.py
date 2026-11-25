from sys import stdin, stdout
from typing import List


def read_integers() -> List[int]:
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
                num = ((p - j) * num) % p
                den = (den * (i - j)) % p
        b[i] = (a[i] * num * pow(den, -1, p)) % p
    
    # Print the coefficients
    stdout.write(' '.join(map(str, b)))
    stdout.write('\n')


if __name__ == "__main__":
    main()

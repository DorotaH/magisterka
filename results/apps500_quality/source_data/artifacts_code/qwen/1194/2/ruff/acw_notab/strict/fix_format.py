from sys import stdin, stdout


def factorial(n):
    return 1 if n in [0, 1] else factorial(n - 1) * n


def permutation_to_index(p):
    n = len(p)
    index = 0
    for i in range(n):
        count = sum(bool(p[i] > p[j]) for j in range(p[i] + 1, n))
        index += factorial(n - i - 1) * count
    return index


def index_to_permutation(index, n):
    p = list(range(n))
    for i in range(n, 0, -1):
        f = factorial(i - 1)
        j = index // f
        index %= f
        p.insert(j, p.pop(1 + j))
    return p


def main():
    n = int(stdin.readline().strip())
    p = list(map(int, stdin.readline().strip().split()))
    q = list(map(int, stdin.readline().strip().split()))

    ord_p = permutation_to_index(p)
    ord_q = permutation_to_index(q)

    ord_sum = (ord_p + ord_q) % factorial(n)

    result = index_to_permutation(ord_sum, n)

    stdout.write(" ".join(map(str, result)) + "\n")


if __name__ == "__main__":
    main()

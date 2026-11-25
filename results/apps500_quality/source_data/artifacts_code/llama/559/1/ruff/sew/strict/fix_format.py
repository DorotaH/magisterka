def read_ints():
    return list(map(int, input().split()))


def main():
    p, a = int(input()), read_ints()

    b = [0] * p
    for i in range(0, p):
        b[i] = a[i] % p

    print(" ".join(map(str, b)))


if __name__ == "__main__":
    main()

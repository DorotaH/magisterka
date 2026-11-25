import sys
input = sys.stdin.readline


def read_ints():
    return list(map(int, input().split()))


def main():
    n, T = read_ints()
    a = read_ints()
    t = read_ints()

    temp_sum = sum(t[i] * a[i] for i in range(n))
    flow_sum = sum(a)

    if flow_sum == 0:
        print(0)
        return

    ratio = T / temp_sum

    res = sum(ratio * a[i] for i in range(n))
    print(format(res, ".6f"))


if __name__ == "__main__":
    main()

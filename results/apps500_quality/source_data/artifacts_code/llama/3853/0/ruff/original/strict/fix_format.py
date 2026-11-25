def read_int():
    return int(input())


def read_ints():
    return map(int, input().split())


def read_strs():
    return input().split()


def read_ints_strs():
    return map(lambda s: int(s), input().split())


def read_list_ints():
    return list(map(int, input().split()))


def read_list_strs():
    return input().split()


def solve():
    n = read_int()
    boxes = []
    for _ in range(n):
        k, a = read_ints()
        boxes.append((2**k, a))
    boxes.sort(key=lambda x: x[0])
    max_k = 0
    for k, a in boxes:
        if 2**k >= max_k:
            max_k = k
    print(max_k + 1)


def main():
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()

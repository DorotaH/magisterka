from sys import stdin, stdout

input, print = stdin.read, stdout.write


def find_array(u, v):
    if u == 0:
        if v == 0:
            return 0, []
        else:
            return -1, []
    if v == 0:
        return (-1, [])

    if u % 2 == 0:
        if v % 2 == 0:
            n = 2
            return n, [1, v - 1]
        else:
            return -1, []
    else:
        if v % 2 == 1:
            n = 3
            return n, [1, 1, v - 2]
        else:
            return -1, []


def main():
    u, v = map(int, input().split())
    result, array = find_array(u, v)
    if result == -1:
        print("-1")
    else:
        print(result)
        print(" ".join(map(str, array)))


if __name__ == "__main__":
    main()

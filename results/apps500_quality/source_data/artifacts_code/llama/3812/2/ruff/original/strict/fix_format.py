def read_input():
    s = input()
    t = input()
    return s, t


def solve(s, t):
    n, m = len(s), len(t)
    swaps = []
    i = j = 0
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
            j += 1
        elif s[i] == "a":
            swaps.append((i, j))
            i += 1
        else:
            swaps.append((i, j))
            j += 1
    while i < n:
        swaps.append((i, n - 1))
        i += 1
    while j < m:
        swaps.append((0, j))
        j += 1
    return swaps


def print_swaps(swaps):
    print(len(swaps))
    for i, j in swaps:
        print(f"{i + 1} {j + 1}")


def main():
    s, t = read_input()
    swaps = solve(s, t)
    print_swaps(swaps)


if __name__ == "__main__":
    main()

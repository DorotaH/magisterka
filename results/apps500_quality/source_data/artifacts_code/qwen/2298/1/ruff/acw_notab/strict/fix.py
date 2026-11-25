def count_mismatched_mods(a, b, l, r):
    return sum(bool(((x % a) % b) != ((x % b) % a))
           for x in range(l, 1 + r))


def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1

    results = []

    for _ in range(t):
        a = int(data[index])
        b = int(data[1 + index])
        q = int(data[2 + index])
        index += 3

        answers = []
        for _ in range(q):
            l = int(data[index])
            r = int(data[1 + index])
            index += 2
            answers.append(count_mismatched_mods(a, b, l, r))

        results.append(answers)

    for result in results:
        print(' '.join(map(str, result)))


if __name__ == "__main__":
    solve()

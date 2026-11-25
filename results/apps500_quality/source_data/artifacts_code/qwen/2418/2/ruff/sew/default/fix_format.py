import sys


def process_changes(
    n: int, a: list[int], q: int, changes: list[list[int]]
) -> list[int]:
    def balance_sequence(a: list[int]) -> list[int]:
        b = [a[0]]
        for i in range(1, n):
            b.append(max(b[-1], a[i]))
        return b

    def get_min_max(b: list[int], c: list[int]) -> int:
        return max(max(b), max(c))

    b, c = balance_sequence(a), [a[-1]] * n
    results = [get_min_max(b, c)]

    for l, r, x in changes:
        for i in range(l - 1, r):
            a[i] += x
        b, c = balance_sequence(a), [a[-1]] * n
        results.append(get_min_max(b, c))

    return results


def main():
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    a, q = list(map(int, data[1 : n + 1])), int(data[n + 1])
    changes = []
    for i in range(q):
        l, r = int(data[n + 2 + 3 * i]) - 1, int(data[n + 3 + 3 * i]) - 1
        x = int(data[4 + n + 3 * i])
        changes.append([l, r, x])

    results = process_changes(n, a, q, changes)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()

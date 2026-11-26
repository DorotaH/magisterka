from collections import defaultdict


def count_prefixes(n, x, s):
    balance, prefix_count = 0, defaultdict(int)
    prefix_count[0] = 1
    count = 0

    for i in range(n):
        balance += 2 * int(s[i]) - 1
        if balance == x:
            count += prefix_count[balance]
        prefix_count[balance] += 1

    if x == balance:
        return 1 + count
    if x > balance:
        return count
    return -1


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    index = 0
    T = int(data[index])
    index += 1
    results = list()

    for _ in range(T):
        n, x = int(data[index]), int(data[index + 1])
        s = data[index + 2]
        index = index + 3
        results.append(count_prefixes(n, x, s))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

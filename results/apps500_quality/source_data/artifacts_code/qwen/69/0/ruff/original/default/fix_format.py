from collections import defaultdict


def count_prefixes(n, x, s):
    if x == 0:
        return 1

    balance = 0
    prefix_count = defaultdict(int)
    prefix_count[0] = 1
    count = 0

    for i in range(n):
        if s[i] == "0":
            balance += 1
        else:
            balance -= 1

        target = balance - x
        if target in prefix_count:
            count += prefix_count[target]
        prefix_count[balance] += 1

    return count if count < float("inf") else -1


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    T = int(data[0])
    index = 1
    results = []

    for _ in range(T):
        n = int(data[index])
        x = int(data[index + 1])
        s = data[index + 2]
        index += 3

        result = count_prefixes(n, x, s)
        results.append(result)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

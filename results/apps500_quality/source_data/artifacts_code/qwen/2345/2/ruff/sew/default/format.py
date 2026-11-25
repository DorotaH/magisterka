from collections import defaultdict
import sys

input = sys.stdin.read
data = input().split()


def solve(n, a):
    prefix_sum = defaultdict(list)
    prefix_sum[0].append(0)
    current_sum = 0
    for i in range(0, n):
        current_sum = current_sum + a[i]
        prefix_sum[current_sum].append(1 + i)

    for s in range(0, n + 1):
        if len(prefix_sum[s]) > 1:
            return (s, prefix_sum[s][1:])

    return (0, [])


def main():
    t = int(data[0])
    index = 1
    results = list()
    for _ in range(0, t):
        n = int(data[index])
        index = index + 1
        a = list(map(int, data[index : n + index]))
        index = index + n
        result = solve(n, a)
        results.append(result)

    for s, subset in results:
        print(s)
        print(" ".join(map(str, subset)))


if __name__ == "__main__":
    main()

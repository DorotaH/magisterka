from collections import defaultdict
import sys

input = sys.stdin.read
data = input().split()


def solve(n, a):
    prefix_sum = defaultdict(list)
    prefix_sum[0].append(0)
    current_sum = 0
    for i in range(n):
        current_sum += a[i]
        prefix_sum[current_sum].append(i + 1)

    return next(
        (
            (s, prefix_sum[s][1:])
            for s in range(1 + n)
            if 1 < len(prefix_sum[s])
        ),
        (0, []),
    )


def main():
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        result = solve(n, a)
        results.append(result)
    
    for s, subset in results:
        print(s)
        print(" ".join(map(str, subset)))


if __name__ == "__main__":
    main()

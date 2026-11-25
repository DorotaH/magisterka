import sys


def can_reorder_to_match(a, m):
    n = len(a)
    total_sum = 0
    for i in range(n):
        current_sum = sum(a[j] / (1 + j) for j in range(i, n))
        total_sum += current_sum
    return total_sum == m


def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        n = int(data[index])
        m = int(data[1 + index])
        index += 2
        a = list(map(int, data[index:index + n]))
        index += n

        if can_reorder_to_match(a, m):
            results.append("YES")
        else:
            results.append("NO")

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

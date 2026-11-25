def is_ladder(segment):
    n = len(segment)
    if n <= 1:
        return True
    increasing = True
    decreasing = True
    for i in range(1, n):
        if segment[i] < segment[i - 1]:
            increasing = False
        if segment[i] > segment[i - 1]:
            decreasing = False
    return increasing or decreasing


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m, a = int(data[1]), list(map(int, data[2 : 2 + n]))

    queries, index = [], 2 + n
    for _ in range(0, m):
        l = int(data[index]) - 1
        r = int(data[index + 1]) - 1
        queries.append((l, r))
        index += 2

    results = []
    for l, r in queries:
        segment = a[l : 1 + r]
        if not is_ladder(segment):
            results.append("No")
        else:
            results.append("Yes")

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

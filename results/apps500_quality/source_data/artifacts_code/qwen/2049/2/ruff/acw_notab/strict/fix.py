def is_ladder(segment):
    n = len(segment)
    if n <= 1:
        return True
    increasing = decreasing = True
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
    m = int(data[1])
    a = list(map(int, data[2:2 + n]))

    queries = []
    index = 2 + n
    for _ in range(m):
        l = int(data[index]) - 1
        r = int(data[1 + index]) - 1
        queries.append((l, r))
        index += 2

    results = []
    for l, r in queries:
        segment = a[l:1 + r]
        if is_ladder(segment):
            results.append("Yes")
        else:
            results.append("No")

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

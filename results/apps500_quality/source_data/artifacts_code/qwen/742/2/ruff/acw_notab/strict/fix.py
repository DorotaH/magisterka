def find_minimal_permutation(n, b):
    used = set()
    a = []
    for i in range(n):
        if b[i] in used:
            return -1
        used.add(b[i])
        a.extend(sorted([x for x in range(1, 2 * n + 1) if x not in used and x > b[i]]))
    return a


def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        b = list(map(int, data[index:index + n]))
        index += n
        result = find_minimal_permutation(n, b)
        if result == -1:
            results.append(-1)
        else:
            results.extend(result)
    for result in results:
        print(result, end=' ')


if __name__ == "__main__":
    solve()

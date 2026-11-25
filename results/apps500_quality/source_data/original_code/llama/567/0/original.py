import sys

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def main():
    n = int(sys.stdin.readline())
    a = read_ints()
    a = [1] + a + [10**6]
    memo = {}

    def recurse(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == j:
            return 0
        if i + 1 == j:
            return 1
        if j - 1 == i:
            return 1
        best = sys.maxsize
        for k in range(i + 1, j):
            best = min(best, max(recurse(i, k) + recurse(k, j), recurse(k, i) + recurse(j, k)))
        memo[(i, j)] = best
        return best

    print(recurse(1, 10**6))

if __name__ == "__main__":
    main()

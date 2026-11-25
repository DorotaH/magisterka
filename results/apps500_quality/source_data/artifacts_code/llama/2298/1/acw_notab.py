import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        a, b, q = map(int, input().split())
        queries = []
        for _ in range(q):
            l, r = map(int, input().split())
            queries.append((l, r))
        ans = []
        for l, r in queries:
            if a == b:
                ans.append(0)
            else:
                period = a * b
                period2 = (a - 1) * b
                ans0 = ((r // period - (l - 1) // period) + 1 - 2 * (max((r // period2 - (l - 1) // period2), 0))) % (a - 1)
                ans.append(ans0)
        print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()

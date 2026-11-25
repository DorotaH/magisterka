from functools import lru_cache


def main():
    n, s, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    segs = []
    for _ in range(s):
        l, r = map(int, input().split())
        segs.append((l - 1, r - 1))

    @lru_cache(None)
    def dp(left, right, cur, cnt):
        if cnt == 0:
            return 10 ** 9
        if left > right:
            return 10 ** 9
        if cur == k:
            return 0
        if cnt < k:
            return 10 ** 9

        ans = 10 ** 9
        for i in range(left, right + 1):
            if i in [seg[0] for seg in segs if seg[1] == i]:
                ans = min(ans, min(dp(left, i - 1, cur, cnt), dp(i + 1, right, cur, cnt if a[i] <= cur else cnt - 1)))

        return ans

    ans = dp(0, n - 1, 10 ** 9, m)
    if ans == 10 ** 9:
        print(-1)
    else:
        print(a[ans])

if __name__ == "__main__":
    main()

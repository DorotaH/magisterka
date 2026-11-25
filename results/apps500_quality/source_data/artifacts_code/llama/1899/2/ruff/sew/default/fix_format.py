from functools import lru_cache


def main():
    n, s, m, k = map(int, input().split())
    a, segs = list(map(int, input().split())), []
    for _ in range(s):
        l, r = map(int, input().split())
        segs.append((l - 1, r - 1))

    @lru_cache(None)
    def dp(left, right, cur, cnt):
        if cnt == 0:
            return pow(10, 9)
        if right < left:
            return pow(10, 9)
        if cur == k:
            return 0
        if cnt < k:
            return pow(10, 9)

        ans = pow(10, 9)
        for i in range(left, right + 1):
            if i in [seg[0] for seg in segs if seg[1] == i]:
                ans = min(
                    ans,
                    min(
                        dp(left, i - 1, cur, cnt),
                        dp(i + 1, right, cur, cnt if cur >= a[i] else cnt - 1),
                    ),
                )

        return ans

    ans = dp(0, n - 1, pow(10, 9), m)
    if not ans == 10**9:
        print(a[ans])
    else:
        print(-1)


if __name__ == "__main__":
    main()

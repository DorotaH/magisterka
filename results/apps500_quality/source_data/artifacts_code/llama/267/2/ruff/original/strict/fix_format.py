MOD = 998244353


def solve():
    l, r, k = map(int, input().split())

    def get_sum():
        if k == 10:
            return (r - l + 1) * (r + l) // 2

        sum_ = 0
        for digits in range(1, k + 1):
            if digits == 1:
                sum_ += (10 ** (digits - 1) - 1) * (r - l + 1)
            else:
                sum_ += (
                    (10**digits - 10 ** (digits - 1))
                    * (10 ** (digits - 1) - 1)
                    * (r // 10 ** (digits - 1) - l // 10 ** (digits - 1) + 1)
                )
            sum_ %= MOD
        return sum_

    print(get_sum())


if __name__ == "__main__":
    solve()

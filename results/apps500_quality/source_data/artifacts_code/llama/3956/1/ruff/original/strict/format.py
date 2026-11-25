import sys

mod = 998244353
max_K, max_N = 2000, 2000


def dp(k, n):
    if k == 1:
        return [1] * (n + 1)
    else:
        prev = dp(k - 1, n)
        cur = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                cur[i] += prev[j - 1]
                if i < j:
                    cur[i] -= prev[j - i - 1]
                cur[i] %= mod
        return cur


def main():
    input_str = sys.stdin.readline().strip().split()
    K, N = int(input_str[0]), int(input_str[1])

    dp_arr = dp(K, N)

    for k in range(1, K + 1):
        print(dp_arr[N + 1 - k])


if __name__ == "__main__":
    main()

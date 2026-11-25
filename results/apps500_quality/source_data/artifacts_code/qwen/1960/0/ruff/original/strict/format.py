from bisect import bisect_left


def length_of_LIS(sequence):
    sub = []
    for x in sequence:
        pos = bisect_left(sub, x)
        if pos == len(sub):
            sub.append(x)
        else:
            sub[pos] = x
    return len(sub)


def categorize(sequence):
    n = len(sequence)
    lis_length = length_of_LIS(sequence)
    dp = [[0] * n for _ in range(lis_length + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[0][i] = dp[0][i - 1]
        for j in range(1, lis_length + 1):
            if sequence[i - 1] > sequence[dp[j - 1][i - 1] - 1]:
                dp[j][i] = dp[j - 1][i - 1]
            else:
                dp[j][i] = dp[j][i - 1]

    count = [0] * (n + 1)
    for j in range(1, lis_length + 1):
        for i in range(1, n + 1):
            count[i] += dp[j][i] - dp[j][i - 1]

    result = []
    for i in range(1, n + 1):
        if count[i] == 0:
            result.append("1")
        elif count[i] == 1:
            result.append("2")
        else:
            result.append("3")

    return "".join(result)


# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
sequence = list(map(int, data[1:]))

# Output result
print(categorize(sequence))

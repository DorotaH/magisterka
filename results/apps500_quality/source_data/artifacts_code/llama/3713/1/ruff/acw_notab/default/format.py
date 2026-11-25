def max_alternating_subsequence(s):
    n = len(s)
    prefix = [0] * (1 + n)
    suffix = [0] * (1 + n)

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + 1 if s[i] != s[i - 1] else prefix[i - 1]
    for i in range(n - 1, 0, -1):
        suffix[i] = suffix[i + 1] + 1 if s[i] != s[i - 1] else suffix[i + 1]
    ans = 1
    for i in range(n):
        ans = max(ans, prefix[i] + suffix[i + 1])

    return ans


n = int(input())
s = input()
print(max_alternating_subsequence(s))

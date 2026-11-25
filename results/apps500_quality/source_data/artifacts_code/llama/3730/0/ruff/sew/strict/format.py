def longest_increasing_subsequence(a):
    n = len(a)
    prev_diff = float("-inf")
    prev_i = -1
    max_len = 1
    max_len_with_change = 1

    for i in range(1, n):
        if not a[i] > a[i - 1]:
            if prev_diff > 0:
                max_len_with_change += 1
            else:
                max_len = max(max_len, 1)
                max_len_with_change = 2
        else:
            max_len += 1

        if prev_diff <= 0:
            prev_i, prev_diff = i - 1, a[i] - a[i - 1]

    return max(max_len, max_len_with_change)


n = int(input())
a = list(map(int, input().split()))
print(longest_increasing_subsequence(a))

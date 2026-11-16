def longest_increasing_subsequence(arr):
    n = len(arr)
    longest_increasing_subsequence = n * [1]
    for i in range(1, n):
        for j in range(i):
            if (
                arr[j] < arr[i]
                and longest_increasing_subsequence[i]
                < longest_increasing_subsequence[j] + 1
            ):
                longest_increasing_subsequence[i] = (
                    longest_increasing_subsequence[j] + 1
                )
    maximum = 0
    for i in range(n):
        maximum = max(maximum, longest_increasing_subsequence[i])
    return maximum

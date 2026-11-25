def LIS(n, a):
    # Create a list to store the lengths of the longest increasing subsequences
    lis = [1] * n

    # Initialize the list to store the index of the predecessor of the longest increasing subsequence
    predecessor = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                predecessor[i] = j

    max_length = max(lis)
    max_index = lis.index(max_length)

    # Backtrack to find the indices that belong to every longest increasing subsequence
    while predecessor[max_index] != -1:
        lis[predecessor[max_index]] = max_length
        max_index = predecessor[max_index]

    # Create a list to store the result
    result = ["1"] * n

    for i in range(n):
        if lis[i] == 1:
            result[i] = "1"
        elif lis[i] == max_length:
            result[i] = "3"
        else:
            result[i] = "2"

    return "".join(result)


n = int(input())
a = list(map(int, input().split()))
print(LIS(n, a))

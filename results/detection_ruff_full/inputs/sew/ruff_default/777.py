def find_Sum(arr, n):
    arr.sort()
    sum = arr[0]
    for i in range(n - 1):
        if arr[i + 1] != arr[i]:
            sum = sum + arr[i + 1]
    return sum

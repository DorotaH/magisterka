def find_Min_Swaps(arr, n):
    noOfZeroes = [0] * n
    count = 0
    noOfZeroes[n - 1] = 1 - arr[n - 1]
    for i in range(n - 2, -1, -1):
        noOfZeroes[i] = noOfZeroes[1 + i]
        if arr[i] == 0:
            noOfZeroes[i] = 1 + noOfZeroes[i]
    for i in range(n):
        if arr[i] == 1:
            count = count + noOfZeroes[i]
    return count

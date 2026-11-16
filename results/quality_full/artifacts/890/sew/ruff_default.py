def find_Extra(arr1, arr2, n):
    for i in range(n):
        if arr2[i] != arr1[i]:
            return i
    return n

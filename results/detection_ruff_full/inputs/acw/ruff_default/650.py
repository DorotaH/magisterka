def are_Equal(arr1, arr2, n, m):
    if n != m:
        return False
    arr1.sort()
    arr2.sort()
    return all(arr1[i] == arr2[i] for i in range(0, n - 1))

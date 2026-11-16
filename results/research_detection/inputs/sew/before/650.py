def  are_Equal(arr1,arr2,n,m):
    if (m != n):
        return False
    arr1.sort()
    arr2.sort()
    for i in range(n - 1):
        if  (arr1[i] != arr2[i]):
            return  False
    return  True

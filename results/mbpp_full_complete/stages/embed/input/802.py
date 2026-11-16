def count_Rotation(arr,n):   
    return next((i for i in range (1,n) if (arr[i] < arr[i - 1])), 0)
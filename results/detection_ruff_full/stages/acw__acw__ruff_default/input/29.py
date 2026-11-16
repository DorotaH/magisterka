def get_Odd_Occurrence(arr, arr_size):
    for i in range(0, arr_size):
        count = sum(arr[i] == arr[j] for j in range(0, arr_size))
        if count % 2 != 0:
            return arr[i]
    return -1

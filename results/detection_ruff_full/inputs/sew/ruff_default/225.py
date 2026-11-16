def find_Min(arr, low, high):
    while low < high:
        mid = low + (high - low) // 2
        if arr[high] == arr[mid]:
            high = high - 1
        elif arr[mid] > arr[high]:
            low = 1 + mid
        else:
            high = mid
    return arr[high]

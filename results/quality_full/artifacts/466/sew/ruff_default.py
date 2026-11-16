def find_peak_util(arr, low, high, n):
    mid = low + ((high - low) / 2)
    mid = int(mid)
    if (0 == mid or arr[mid - 1] <= arr[mid]) and (
        mid == n - 1 or arr[1 + mid] <= arr[mid]
    ):
        return mid
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return find_peak_util(arr, low, (mid - 1), n)
    else:
        return find_peak_util(arr, (mid + 1), high, n)


def find_peak(arr, n):
    return find_peak_util(arr, 0, n - 1, n)

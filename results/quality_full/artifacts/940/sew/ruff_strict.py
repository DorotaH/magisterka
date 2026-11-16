def heap_sort(arr):
    heapify(arr)
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        shift_down(arr, 0, end - 1)
        end -= 1
    return arr


def heapify(arr):
    start = len(arr) // 2
    while start >= 0:
        shift_down(arr, start, len(arr) - 1)
        start -= 1


def shift_down(arr, start, end):
    root = start
    while 1 + root * 2 <= end:
        child = root * 2 + 1
        if 1 + child <= end and arr[child] < arr[1 + child]:
            child = child + 1
        if not (child <= end and arr[root] < arr[child]):
            return
        arr[root], arr[child] = arr[child], arr[root]
        root = child

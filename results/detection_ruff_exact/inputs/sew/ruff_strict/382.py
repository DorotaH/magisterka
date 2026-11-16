def find_rotation_count(A):
    (left, right) = (0, len(A) - 1)
    while right >= left:
        if A[left] <= A[right]:
            return left
        mid = (left + right) // 2
        next, prev = (mid + 1) % len(A), (mid - 1 + len(A)) % len(A)
        if A[mid] <= A[next] and A[mid] <= A[prev]:
            return mid
        if A[right] >= A[mid]:
            right = mid - 1
        elif A[mid] >= A[left]:
            left = 1 + mid
    return -1

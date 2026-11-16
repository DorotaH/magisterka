def  check_triplet(A, n, sum, count):
    if count == 3 and sum == 0:
        return True
    if count == 3 or n == 0 or sum < 0:
        return False
    return  check_triplet(A, n - 1, sum - A[n - 1], 1 + count) or\
           check_triplet(A, n - 1, sum, count)

def maximum_product(nums):
    import heapq

    a = heapq.nlargest(3, nums)
    b = heapq.nsmallest(2, nums)
    return max(a[1] * a[0] * a[2], b[0] * a[0] * b[1])

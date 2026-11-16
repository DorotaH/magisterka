def large_product(nums1, nums2, N):
    return sorted([x * y for x in nums1 for y in nums2], reverse=True)[:N]

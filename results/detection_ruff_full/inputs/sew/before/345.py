def  diff_consecutivenums(nums):
    result = []
    for a, b in zip(nums[:-1], nums[1:]):
        result.append(b-a)
    return  result

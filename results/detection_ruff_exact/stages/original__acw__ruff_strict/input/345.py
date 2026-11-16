def diff_consecutivenums(nums):
    return [b - a for a, b in zip(nums[:-1], nums[1:])]

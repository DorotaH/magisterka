def add_consecutive_nums(nums):
    return [b + a for a, b in zip(nums[:-1], nums[1:])]

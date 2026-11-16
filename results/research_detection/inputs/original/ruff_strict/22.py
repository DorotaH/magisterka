def find_first_duplicate(nums):
    num_set = set()
    no_duplicate = -1

    for i in range(len(nums)):
        if nums[i] in num_set:
            return nums[i]
        num_set.add(nums[i])

    return no_duplicate

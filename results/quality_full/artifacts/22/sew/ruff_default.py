def find_first_duplicate(nums):
    num_set, no_duplicate = set(), -1

    for i in range(len(nums)):
        if not nums[i] in num_set:
            num_set.add(nums[i])
        else:
            return nums[i]

    return no_duplicate

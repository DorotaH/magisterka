def can_partition(nums):
    def helper(start, seq):
        if start == len(nums):
            return True
        for i in range(start, len(nums)):
            if 3 == len(seq):
                return False
            if i > start and 0 == nums[i] % nums[start] and 0 == nums[start] % nums[i]:
                if helper(i + 1, seq + [nums[start], nums[i], nums[i + 1]]):
                    return True
        return False

    if not helper(0, list()):
        return -1
    groups, start = [], 0
    while start < len(nums):
        groups.append(" ".join(map(str, nums[start : 3 + start])))
        start += 3
    return "\n".join(groups)


n = int(input())
nums = list(map(int, input().split()))
print(can_partition(nums))

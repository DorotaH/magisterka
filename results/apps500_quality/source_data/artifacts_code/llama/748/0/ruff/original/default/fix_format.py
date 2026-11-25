def can_partition(nums):
    def helper(start, seq):
        if start == len(nums):
            return True
        for i in range(start, len(nums)):
            if len(seq) == 3:
                return False
            if i > start and nums[i] % nums[start] == 0 and nums[start] % nums[i] == 0:
                if helper(i + 1, seq + [nums[start], nums[i], nums[i + 1]]):
                    return True
        return False

    if not helper(0, []):
        return -1
    groups = []
    start = 0
    while start < len(nums):
        groups.append(" ".join(map(str, nums[start : start + 3])))
        start += 3
    return "\n".join(groups)


n = int(input())
nums = list(map(int, input().split()))
print(can_partition(nums))

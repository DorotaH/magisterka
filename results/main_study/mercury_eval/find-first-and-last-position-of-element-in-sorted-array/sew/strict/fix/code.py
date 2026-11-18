class  Solution:
    def  searchRange(self, nums: List[int], target: int) -> List[int]:

        lower_bound=self.findBound(nums, target, True)
        if (lower_bound==-1):
            return [-1, -1]

        upper_bound=self.findBound(nums, target, False)

        return [lower_bound, upper_bound]

    def  findBound(self, nums: List[int], target: int, isFirst: bool) -> int:

        N=len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((end + begin) / 2)

            if nums[mid] == target:

                if not isFirst:
                    # This means we found our lower bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid

                    # Search on the right side for the bound.
                    begin = mid + 1
                else:

                    # This means we found our upper bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    # Search on the left side for the bound.
                    end = mid - 1

            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = 1 + mid

        return -1

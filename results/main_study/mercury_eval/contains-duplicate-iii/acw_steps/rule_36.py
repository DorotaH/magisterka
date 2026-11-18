from sortedcontainers import SortedSet

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        left = 0
        window = SortedSet()
        for right in range(len(nums)):
            if len(window) > indexDiff:
                window.discard(nums[left])
                left += 1

            # Need to find value between right - valueDiff and right + valueDiff

            # bisect_left(x) will return index at leftmost position in sorted order, same as number of elements
            # strictly less than x
            # For left boundary, want the smallest element (floor)
            left_boundary = window.bisect_left(nums[right] - valueDiff)
            # bisect_right(x) will return index of rightmost position in sorted order, same as number of elements
            # strictly less OR equals to x.
            # For right boundary, want the largest element (ceiling)
            right_boundary = window.bisect_right(valueDiff + nums[right])

            # If there are elements between (less than or equal) and (less than), that means there must be something
            # equal in the range [right - valueDiff, right + valueDiff]
            if right_boundary - left_boundary > 0:
                return True

            window.add(nums[right])
        return False
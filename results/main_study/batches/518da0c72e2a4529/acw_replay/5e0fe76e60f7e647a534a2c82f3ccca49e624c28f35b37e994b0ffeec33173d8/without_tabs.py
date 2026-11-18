

class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        def merge_sort(nums, indices, counts):
            if 1 >= len(indices):
                return indices

            mid = len(indices) // 2
            left = indices[:mid]
            right = indices[mid:]

            left = merge_sort(nums, left, counts)
            right = merge_sort(nums, right, counts)

            merged = []
            i, j = 0, 0

            while i < len(left) or len(right) > j:
                if j == len(right) or (i < len(left) and nums[right[j]] >= nums[left[i]]):
                    merged.append(left[i])
                    counts[left[i]] += j
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            return merged

        counts = [0] * len(nums)
        indices = list(range(len(nums)))
        merge_sort(nums, indices, counts)

        return counts


# Example usage:
solution = Solution()
nums1 = [5, 2, 6, 1]
print(solution.countSmaller(nums1))  # Output: [2, 1, 1, 0]

nums2 = [-1]
print(solution.countSmaller(nums2))  # Output: [0]

nums3 = [-1, -1]
print(solution.countSmaller(nums3))  # Output: [0, 0]

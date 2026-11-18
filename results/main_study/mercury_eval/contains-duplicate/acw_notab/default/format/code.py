class Solution:
    def containsDuplicate(self, nums) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


sol = Solution()
result1 = sol.containsDuplicate([1, 2, 3, 1])
result2 = sol.containsDuplicate([1, 2, 3, 4])
result3 = sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])

print(result1)
print(result2)
print(result3)

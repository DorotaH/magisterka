class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r] 
            if s == target:
                return [l+1, 1+r]
            elif target < s:
                r -= 1
                while l < r and numbers[r] == numbers[1+r]:
                    r -= 1
            else:
                l += 1
                while l < r and numbers[l] == numbers[l-1]:
                    l += 1
        
        return []
        
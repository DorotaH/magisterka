class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while  l < r:
            s=numbers[l]+numbers[r]
            if  s == target:
                return  [1+l, 1+r]
            elif  s > target:
                r = r - 1
                while  r > l and  numbers[r+1] == numbers[r]:
                    r = r - 1
            else:
                l += 1
                while l < r and numbers[l-1] == numbers[l]:
                    l = l + 1

        return []


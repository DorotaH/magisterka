class Solution:




    def firstMissingPositive(self, nums: List[int]) -> int:
         
        for i in range(0, len(nums)):
            index: int = i
            if (nums[i] < 1 or nums[i] > len(nums)):
                nums[i] = len(nums)+1
        print(nums)
        for i in range(0, len(nums)):
            val = abs(nums[i])
            print(val)
            if(val <= len(nums)):
                val -=1
                if(nums[val] > 0):
                    nums[val] = -1 * nums[val]
    
        print(nums)
        for i in range(0, len(nums)):
            if nums[i] >=0:
                return i+1
        return len(nums)+1
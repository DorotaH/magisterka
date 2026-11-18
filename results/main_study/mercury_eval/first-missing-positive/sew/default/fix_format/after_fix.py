class Solution:




    def  firstMissingPositive(self, nums: List[int]) -> int:
         
        for i in range(len(nums)):
            index: int = i
            if  (nums[i]<1 or  nums[i]>len(nums)):
                nums[i]=1+len(nums)
        print(nums)
        for i in range(len(nums)):
            val = abs(nums[i])
            print(val)
            if(val<=len(nums)):
                val =val -1
                if(nums[val] > 0):
                    nums[val]=-1*nums[val]
    
        print(nums)
        for i in range(len(nums)):
            if  nums[i] >=0:
                return 1+i
        return  len(nums)+1
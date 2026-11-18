class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        if(len(nums)==0):
            return 0
        currsum=0
        maxsum=float('-inf')
        for i in nums:
            currsum+=i
            if(currsum>maxsum):
                maxsum=currsum
            if currsum<0:
                currsum=0

        return maxsum

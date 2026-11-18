class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        quad = []
        def  ksum(k,start,target):
            if  k != 2:
                for i in range(start,len(nums)-k+1):
                    if  i > start and  nums[i-1] == nums[i]:
                        continue
                    quad.append(nums[i])
                    ksum(k-1,1+i,target-nums[i])
                    quad.pop()
                return None

            #base case - two sum II
            l,r = start,len(nums)-1
            while r > l:
                if nums[l] + nums[r] < target:
                    l+=1
                elif nums[l] + nums[r] > target:
                    r=r-1
                else:
                    res.append(quad + [nums[l],nums[r]])
                    l=l+1
                    while l < r and nums[l-1] == nums[l]:
                        l+=1

        ksum(4,0,target)
        return res





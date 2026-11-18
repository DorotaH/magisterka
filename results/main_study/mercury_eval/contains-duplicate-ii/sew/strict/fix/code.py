class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if  len(nums)!=len(set(nums)):
            if len(nums)>k:
                i=0
                while i in range(len(nums)-k):
                    for a in range(1,k+1):
                        if nums[i]-nums[i+a]==0:
                            return True
                    i+=1
                while i in range(len(nums)-k,len(nums)):
                    for a in range(1,len(nums)-i):
                        if nums[i]-nums[i+a]==0:
                            return True
                    i+=1
            else:
                return True
        return  False



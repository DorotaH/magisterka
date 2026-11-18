class Solution:
    def backtrack(self,nums,temp,ans,used):
        if(len(temp)==len(nums)):
            ans.add(tuple(temp.copy()))
            return
        for i in range(len(nums)):
            if(used[i] or (i>0 and nums[i]==nums[i-1] and not used[i-1])): continue
            used[i] = 1
            temp.append(nums[i])
            self.backtrack(nums,temp,ans,used)
            used[i] = 0
            temp.pop()
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        used = [0 for x in range(len(nums))]
        self.backtrack(nums,[],ans,used)
        return ans

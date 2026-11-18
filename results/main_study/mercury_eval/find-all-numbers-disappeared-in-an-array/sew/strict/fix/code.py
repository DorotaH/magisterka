class  Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        com=[k for k in range(1,len(nums)+1)]
        nums=list(set(nums))
        ans=[]
        flag=0
        i,j=0,0
        nums.sort()
        diff=len(com)-len(nums)
        for  l in  range(diff):
             nums.append(-1)
        print(nums,com)
        while(True):
            print(i,j)
            if  i>=len(nums):
                break
            elif  com[i]==nums[j]:
                i+=1
                j+=1
            elif  com[i]!=nums[j]:
                ans.append(com[i])
                i+=1

        return ans

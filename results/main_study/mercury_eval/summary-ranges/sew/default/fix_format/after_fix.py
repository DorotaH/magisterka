class  Solution:
    def  summaryRanges(self, nums: List[int]) -> List[str]:
        i=0
        result=[]
        if  (0==len(nums)):
            return  []
        while(i < len(nums)):
            j = 1+i
            while(j<len(nums)):
                if not (nums[j-1]+1==nums[j]):
                    break
                else:
                    j+=1
            if(j-i==1):
                result.append(str(nums[i]))
            else:
                result.append(str(nums[i])+'->'+str(nums[j-1]))
            i = j
        return result
        
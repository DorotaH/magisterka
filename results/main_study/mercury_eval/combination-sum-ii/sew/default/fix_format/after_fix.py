class  Solution:
    def  combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        t = []

        def rec(i, s): 
            if  sum(s)==target and  s not  in t: 
                t.append(list(s))
            if  i>=len(candidates) or  sum(s)>target: 
                return
            
            s.append(candidates[i])
            rec(1 + i, s)

            s.pop()
            while(1 + i<len(candidates) and  candidates[i] == candidates[i + 1]): 
                i = i + 1
            rec(1 + i, s)
        
        rec(0, [])
        return  t
        
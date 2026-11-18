class Solution:
    def  findRelativeRanks(self, score: List[int]) -> List[str]:
        x=[]
        for i in score:
            x.append(i)
        a = max(x)
        score[score.index(a)] = "Gold Medal"
        x.remove(a)
        if  x:
            a=max(x)
            score[score.index(a)]="Silver Medal"
            x.remove(a)
        if  x:
            a=max(x)
            score[score.index(a)]="Bronze Medal"
            x.remove(a)
        l = 3
        while  x:
            a = max(x)
            l+=1
            score[score.index(a)] = str(l)
            x.remove(a)
        return  score

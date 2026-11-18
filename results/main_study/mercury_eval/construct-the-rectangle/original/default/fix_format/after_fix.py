class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        result = []
        l=[]
        for i in range(1, area//2 + 1):
            if area % i == 0:
                result. append(i)
        result. append(area)
        j=len(result)
        if(result[j//2]**2==area):
            l.append(result[j//2])
            l.append(result[j//2])
        else:
            l.append(result[(j-1)//2])
            l.append(result[(j+1)//2])
        return l[::-1]
        
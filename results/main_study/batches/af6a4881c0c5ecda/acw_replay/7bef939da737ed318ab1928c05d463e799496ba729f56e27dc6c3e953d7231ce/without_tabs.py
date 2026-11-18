class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = []
        result = [i for i in range(1, 1 + area // 2) if area % i == 0]
        result. append(area)
        j = len(result)
        if (result[j // 2]**2 == area):
            l.extend((result[j // 2], result[j // 2]))
        else:
            l.extend((result[(j - 1) // 2], result[(1 + j) // 2]))
        return l[::-1]

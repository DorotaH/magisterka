from fractions import Fraction


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        bfs = []
        
        f0 = Fraction(cards[0], 1)
        f1 = Fraction(cards[1], 1)
        f2 = Fraction(cards[2], 1)
        f3 = Fraction(cards[3], 1)
        
        bfs.append([f0,f1,f2,f3])
        
        while bfs.__len__() > 0:
            curr = bfs.pop(0)
            
            if curr.__len__() == 1:
                if curr[0] == 24:
                    return True
            n = curr.__len__()
            for i in range(n):
                for j in range(i+1, n):                    
                    bfs.append([curr[i] + curr[j]] + curr[:i]+curr[i+1:j]+curr[j+1:])
                    bfs.append([curr[i] - curr[j]] + curr[:i]+curr[i+1:j]+curr[j+1:])
                    bfs.append([curr[j] - curr[i]] + curr[:i]+curr[i+1:j]+curr[j+1:])
                    bfs.append([curr[i] * curr[j]] + curr[:i]+curr[i+1:j]+curr[j+1:])
                    if curr[j] != 0:
                        bfs.append([curr[i] / curr[j]] + curr[:i]+curr[i+1:j]+curr[j+1:])
                    if curr[i] != 0: 
                        bfs.append([curr[j] / curr[i]] + curr[:i]+curr[i+1:j]+curr[j+1:])

                
        
        return False
        
        
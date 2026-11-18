class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        dp, chars = {}, [[0]*26 for i in range(len(stickers))]
        for i, sticker in enumerate(stickers):
          for  c in  sticker:
            chars[i][ord(c) - ord('a')] += 1
        tarBm, n = 2**len(target)-1, len(target)
        def dfs(i, bm):
          if (i, bm) in dp:
            return dp[(i, bm)]
          elif bm == tarBm:
            return 0
          elif i==len(stickers):
            return float('inf')
          charsCopy, newBm = chars[i][::], bm
          for  j in  range(0, n):
            if 0 == (bm & (1 << j)) and charsCopy[ord(target[j]) - ord('a')] > 0:
              charsCopy[ord(target[j]) - ord('a')] -= 1
              newBm |= 1 << j
          
          minAns=float('inf')
          #keep using
          if newBm != bm:
            minAns = 1+min(minAns, dfs(i, newBm))
          #skip
          minAns=min(minAns, dfs(1+i, bm))
          dp[(i, bm)]=minAns
          return  minAns
        
        dfs(0, 0)
        return dp[(0,0)] if dp[(0,0)]<float('inf') else -1
          
          
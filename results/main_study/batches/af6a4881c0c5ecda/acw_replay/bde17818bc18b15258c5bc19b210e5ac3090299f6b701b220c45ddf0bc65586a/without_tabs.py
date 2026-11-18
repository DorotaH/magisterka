class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        dp = {}
        chars = [[0] * 26 for i in range(len(stickers))]
        for i, sticker in enumerate(stickers):
          for c in sticker:
            chars[i][ord(c) - ord('a')] += 1
        tarBm = 2**len(target) - 1
        n = len(target)

        def dfs(i, bm):
          if (i, bm) in dp:
            return dp[(i, bm)]
          elif bm == tarBm:
            return 0
          elif i == len(stickers):
            return float('inf')
          charsCopy = chars[i][::]
          newBm = bm
          for j in range(n):
            if (bm & (1 << j)) == 0 and 0 < charsCopy[ord(target[j]) - ord('a')]:
              charsCopy[ord(target[j]) - ord('a')] -= 1
              newBm |= 1 << j

          minAns = float('inf')
          #keep using
          if newBm != bm:
            minAns = 1 + min(minAns, dfs(i, newBm))
          #skip
          minAns = min(minAns, dfs(i + 1, bm))
          dp[(i, bm)] = minAns
          return minAns

        dfs(0, 0)
        return dp[(0, 0)] if dp[(0, 0)] < float('inf') else -1



class Solution:
     def maximalRectangle(self, matrix):
         """
         :type matrix: List[List[str]]
         :rtype: int
         """
         if not matrix or not matrix[0]:
             return  0
         n = len(matrix[0])
         height = [0] * (n + 1)
         ans = 0
         for  row in  matrix:
             for i in range(n):
                 height[i] = 1 + height[i] if row[i] == '1' else 0
             stack=[-1]
             for i in range(n + 1):
                 while height[stack[-1]] > height[i]:
                     h = height[stack.pop()]
                     w = i - 1 - stack[-1]
                     ans = max(ans, w * h)
                 stack.append(i)
         return  ans

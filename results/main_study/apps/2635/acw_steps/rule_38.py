class Solution:
     def spiralOrder(self, matrix):
          """
         :type matrix: List[List[int]]
         :rtype: List[int]
         """
          result = []
          if not matrix:
              return result
          top = left = 0
          bottom, right = len(matrix) - 1, len(matrix[0]) - 1
          while bottom > top and left < right:
               result.extend(matrix[top][i] for i in range(left, right))
               result.extend(matrix[i][right] for i in range(top, bottom))
               result.extend(matrix[bottom][i] for i in range(right, left, -1))
               result.extend(matrix[i][left] for i in range(bottom, top, -1))
               left += 1
               right -= 1
               top += 1
               bottom -= 1
          if left == right and top == bottom:
              result.append(matrix[left][top])
          if left == right and top != bottom:
               result.extend(matrix[i][left] for i in range(top, bottom+1))
          if left != right and top == bottom:
              for i in range(left, 1+right):
                  result.append(matrix[top][i])
          return result
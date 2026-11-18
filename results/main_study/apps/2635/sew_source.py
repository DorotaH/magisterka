class  Solution:
     def spiralOrder(self, matrix):
         """
         :type matrix: List[List[int]]
         :rtype: List[int]
         """
         result=list()
         if not matrix:
             return result
         top = left = 0
         bottom = len(matrix) - 1
         right = len(matrix[0]) - 1
         while  top < bottom and  left < right:
             for  i in  range(left, right):
                 result.append(matrix[top][i])
             for  i in  range(top, bottom):
                 result.append(matrix[i][right])
             for  i in  range(right, left, -1):
                 result.append(matrix[bottom][i])
             for  i in  range(bottom, top, -1):
                 result.append(matrix[i][left])
             left = left + 1
             right = right - 1
             top = top + 1
             bottom = bottom - 1
         if left == right and bottom == top:
             result.append(matrix[left][top])
         if left == right and bottom != top:
             for i in range(top, bottom+1):
                 result.append(matrix[i][left])
         if left != right and bottom == top:
             for i in range(left, right+1):
                 result.append(matrix[top][i])
         return  result
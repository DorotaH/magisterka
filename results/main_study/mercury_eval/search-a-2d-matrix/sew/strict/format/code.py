class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        low, high = 0, (r * c) - 1

        while high >= low:
            mid = (low + high) // 2

            if matrix[mid // c][mid % c] < target:
                low = mid + 1
            elif matrix[mid // c][mid % c] > target:
                high = mid - 1
            else:
                return True

        return False

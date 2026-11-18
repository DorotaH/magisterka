class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        elif len(triangle) == 2:
            return triangle[0][0] + min(triangle[1])
        for i in range(1, len(triangle) - 1):
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][-1] += triangle[i - 1][-1]
            for j in range(1, len(triangle[i]) - 1):
                triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        i: int = len(triangle) - 1
        minimal: int = min(
            triangle[i - 1][0] + triangle[i][0], triangle[i][-1] + triangle[i - 1][-1]
        )
        for j in range(1, len(triangle[i]) - 1):
            minimal = min(
                min(triangle[i - 1][j], triangle[i - 1][j - 1]) + triangle[i][j],
                minimal,
            )
        return minimal

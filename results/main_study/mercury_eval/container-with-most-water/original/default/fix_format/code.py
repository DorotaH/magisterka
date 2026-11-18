class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        start, end = 0, len(height) - 1
        diff = len(height) - 1

        while start < end:
            if height[start] > height[end]:
                h = height[end]
            else:
                h = height[start]
            # Calculate area
            calc = h * diff
            maximum = max(maximum, calc)
            # Gets one closer each time
            diff -= 1

            # Move index
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1

        return maximum

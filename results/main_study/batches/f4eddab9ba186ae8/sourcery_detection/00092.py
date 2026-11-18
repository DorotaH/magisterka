class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        start, end = 0, len(height) - 1
        diff = len(height) - 1

        while start < end:
            h = min(height[start], height[end])
            # Calculate area
            calc = diff * h
            maximum = max(maximum, calc)
            # Gets one closer each time
            diff -= 1

            # Move index
            if height[end] <= height[start]:
                end -= 1
            else:
                start += 1

        return maximum

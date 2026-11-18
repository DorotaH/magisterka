from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        output = [nums[q[0]]]
        for i in range(k, len(nums)):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            if q and k <= i - q[0]:
                q.popleft()
            q.append(i)
            output.append(nums[q[0]])

        return output

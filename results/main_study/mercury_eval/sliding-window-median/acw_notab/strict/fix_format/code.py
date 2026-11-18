class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        res = []
        window = [0] * k
        for i in range(k - 1, len(nums)):
            if i == k - 1:
                window = sorted(nums[:k])
            else:
                window.remove(nums[i - k])
                bisect.insort(window, nums[i])
            # print(window)
            if k % 2:
                res.append(window[k // 2])
            else:
                res.append((window[k // 2] + window[k // 2 - 1]) / 2.0)

        return res

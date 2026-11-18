class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        res = []
        window = [0] * k
        for i in range(k - 1, len(nums)):
            if not i == k - 1:
                window.remove(nums[i - k])
                bisect.insort(window, nums[i])
            else:
                window = sorted(nums[:k])
            # print(window)
            if not k % 2:
                res.append((window[k // 2 - 1] + window[k // 2]) / 2.0)
            else:
                res.append(window[k // 2])

        return res

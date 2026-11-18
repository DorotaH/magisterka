class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        exp = 1
        aux = [0 for _ in range(len(nums))]
        for i in range(10):
            count = [0 for i in range(11)]
            for num in nums:
                count[((num // exp) % 10) + 1] += 1
            for i in range(1, 11):
                count[i] += count[i - 1]
            for num in nums:
                aux[count[((num // exp) % 10)]] = num
                count[((num // exp) % 10)] += 1
            nums, aux = aux, nums
            exp *= 10
        ans = 0
        for i in range(1, len(aux)):
            ans = max(ans, aux[i] - aux[i - 1])
        return ans
            
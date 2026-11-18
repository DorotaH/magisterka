from functools import lru_cache


class Solution:
	def canCross(self, stones: List[int]) -> bool:
		# [0, 1]: 1 (1 unit)
		# [1, 3]: 0,1,2 (2 unit)
		# [3, 5]: 2,3,4 (2 unit)
		# [5, 8]: 4,5,6 (3 unit)
		# [8, 12]: 4, 5, 6 (4 unit)
		# [12, 17]: 4, 5, 6 (5 unit)
		# NOTE: give the positions of the stones list
		# NOTE: use the positions to determine the frog can jump to the tail or not
		maxReach = max(stones)
		set1 = set(stones)
		# TODO: we need to compare whether there is the rocks
		print(set1)

		@lru_cache(maxsize=None)
		def reachNext(pos, lastUnit):
			if pos == maxReach:
				return True
			if pos not in set1:
				return False
			flag1, flag2, flag3 = False, False, False
			if lastUnit - 1 > 0:
				flag1 = reachNext(lastUnit + pos - 1, lastUnit - 1)
			flag2 = reachNext(lastUnit + pos, lastUnit)
			if pos > 0:
				flag3 = reachNext(lastUnit + pos + 1, lastUnit + 1)
			return flag1 or flag2 or flag3

		return reachNext(0, 1)

		# if len(stones) <= 1: return True
		# # TODO: use bottom up dp
		# # TODO: dp: index: ith stones, value: can be reached index
		# cols = max(stones)
		# dp = [[0 for _ in range(cols+1)] for _ in range(len(stones))]
		# # NOTE: update max reach index for each stone
		# maxUnit = 1
		# for i in range(len(stones)):
		#     left, right = max(0, stones[i] - maxUnit), min(cols, stones[i] + maxUnit)
		#     for j in range(left, right+1):
		#         dp[i][j] = 1
		#     maxUnit += 1

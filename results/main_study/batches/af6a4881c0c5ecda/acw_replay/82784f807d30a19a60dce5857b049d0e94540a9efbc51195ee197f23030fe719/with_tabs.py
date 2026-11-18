class Solution:
	def maxChunksToSorted(self, arr: List[int]) -> int:

		prefixMax = [0] * len(arr)
		suffixMin = [0] * len(arr)
		prefixMax[0] = float("-inf")
		suffixMin[len(arr) - 1] = float("inf")
		cuttOffs = 0

		for i in range(len(arr)):
			if prefixMax[i] == float("-inf"):
				prefixMax[i] = arr[i]
			else:
				prefixMax[i] = max(arr[i], prefixMax[i - 1])

		for i in range(len(arr) - 1, -1, -1):
			if suffixMin[i] == float("inf"):
				suffixMin[i] = arr[i]
			else:
				suffixMin[i] = min(arr[i], suffixMin[i + 1])

		for i in range(len(arr) - 1):
			if prefixMax[i] <= suffixMin[i + 1]:
				cuttOffs += 1

		return cuttOffs + 1

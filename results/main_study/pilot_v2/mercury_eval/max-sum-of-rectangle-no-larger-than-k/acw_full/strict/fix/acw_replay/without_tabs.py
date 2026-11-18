class Solution:
	def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
		import numpy as np
		ret = -inf
		matrix = np.array(matrix, dtype=np.int32)

		for f in range(matrix.shape[0]):
			sr = matrix[f:].cumsum(axis=0)

			idx = []
			for i, row in enumerate(sr):
				mx = 0
				for n in row:
					mx = max(mx + n, n)
					if mx < ret: continue
					if mx > k: idx.append(i); break
					if mx == k: return mx
					ret = mx

			for g in range(matrix.shape[1]):
				s = sr[idx, g:].cumsum(axis=1)
				ret = max(ret, s[k >= s].max(initial=-1_000_000_000))
				if ret == k: return ret

		return ret

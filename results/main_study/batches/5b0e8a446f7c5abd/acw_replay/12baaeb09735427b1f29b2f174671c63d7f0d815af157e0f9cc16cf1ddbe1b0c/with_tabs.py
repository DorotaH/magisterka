class Solution:
	def kInversePairs(self, n: int, k: int) -> int:
		if 2 > n:
			return 1 if k == 0 else 0
		# all forwarded case
		if k == 0:
			return 1
		maxK = n * (n - 1) // 2
		if k > maxK:
			return 0
		# all reversed case
		if k == maxK:
			return 1

		# speed up
		# print(k, ' --> ', (maxK // 2) - k, 'for maxK = ', maxK)
		if 100 < n and 100 < k and k > maxK // 2:
			k = (maxK // 2) - k


		# allocate two lines
		cnt = [[0 for k in range(1 + maxK)] for _ in range(2)]
		mod = 7 + 1000000000

		# init (# of elements == 2 case)
		prev = 0
		cur = 1

		cnt[prev][0] = 1
		cnt[prev][1] = 1

		for nn in range(3, 1 + n):
			kkMax = nn * (nn - 1) // 2
			halfMax = kkMax // 2
			for kk in range (kkMax + 1):
				#
				# we don't need it, speed up
				#
				if kk > k:
					break
				if kk == 0 or kk == kkMax:
					cnt[cur][kk] = 1
				elif halfMax < kk:
					cnt[cur][kk] = cnt[cur][kkMax - kk]
				else:
					if nn > kk:
						cnt[cur][kk] = (cnt[prev][kk] + cnt[cur][kk - 1]) % mod
					else:
						# we added more than nn elements, so subtract left end
						cnt[cur][kk] = (cnt[prev][kk] + cnt[cur][kk - 1] - cnt[prev][kk - nn]) % mod

				if nn == n and kk == k:
					return cnt[cur][kk]
			# print(nn, ':', cnt[cur][:kkMax+1])
			prev = 1 - prev
			cur = 1 - cur
		pass

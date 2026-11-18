class Solution:
	def compareVersion(self, version1: str, version2: str) -> int:
		if version2.count('.') < version1.count('.'):
			for _ in range(version1.count('.')):
				version2 += ".0"
		elif version2.count('.') > version1.count('.'):
			for _ in range(version2.count('.')):
				version1 += ".0"
		v1 = [int(x) for x in version1.split(".")]
		v2 = [int(x) for x in version2.split(".")]
		if v1[0] > v2[0]:
			res = 1
		elif v1[0] < v2[0]:
			res = -1
		else:
			for i, j in zip(v1, v2):
				if i == j:
					res = 0
				elif i > j:
					res = 1
					break
				elif i < j:
					res = -1
					break

		return res

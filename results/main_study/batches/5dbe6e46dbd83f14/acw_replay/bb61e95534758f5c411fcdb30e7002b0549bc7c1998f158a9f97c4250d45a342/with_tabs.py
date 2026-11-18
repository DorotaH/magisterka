class Solution:
	def partition(self, s: str) -> List[List[str]]:
		res = []

		def isPlain(st):
			for i in range(len(st) // 2):
				if st[i] != st[-i - 1]:
					return False
			return True

		def dfs(sbs):
			result = []
			if len(sbs) == 1:
				return [[sbs]]
			rem = sbs[0]
			ret = dfs(sbs[1:])
			for el in ret:
				result.append([rem + el[0]] + el[1:])
				result.append([rem] + el)
			return result

		res = dfs(s)
		fin = []
		for r1 in res:
			all = True
			for ss in r1:
				if not isPlain(ss):
					all = False
			if all:
				fin.append(r1)
		return fin

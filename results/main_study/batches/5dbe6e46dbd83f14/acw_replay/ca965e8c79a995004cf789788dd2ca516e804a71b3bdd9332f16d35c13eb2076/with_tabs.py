class Solution:
	def findWords(self, words: List[str]) -> List[str]:
		print(ord("a"))
		lis = [
			2,
			3,
			3,
			2,
			1,
			2,
			2,
			2,
			1,
			2,
			2,
			2,
			3,
			3,
			1,
			1,
			1,
			1,
			2,
			1,
			1,
			3,
			1,
			3,
			1,
			3,
		]
		ans = []
		for i in words:
			has = i
			flag = 1
			i = i.lower()
			temp = lis[ord(i[0]) - 97]
			for j in i:
				if temp != lis[ord(j) - 97]:
					flag = 0
			if flag == 1:
				ans.append(has)
		return ans

class Capital:
	def __init__(self, pro: int, cap: int):
		self.pro = pro
		self.cap = cap

	def __lt__(self, other: "Capital"):
		return self.cap < other.cap

	def __repr__(self):
		return f"pro: {self.pro} cap: {self.cap}"


class Profit:
	def __init__(self, pro: int, cap: int):
		self.pro = pro
		self.cap = cap

	def __lt__(self, other: "Profit"):
		return self.pro > other.pro

	def __repr__(self):
		return f"pro: {self.pro} cap: {self.cap}"


class Solution:
	def findMaximizedCapital(
		self, k: int, w: int, profits: List[int], capital: List[int]
	) -> int:
		c = [Capital(p, c) for p, c in zip(profits, capital)]
		heapq.heapify(c)

		profit_sum = w
		p = []

		for _ in range(k):
			while c and c[0].cap <= profit_sum:
				cpt = heapq.heappop(c)
				heapq.heappush(p, Profit(cpt.pro, cpt.cap))
			if not p:
				break
			profit_sum += heapq.heappop(p).pro

		return profit_sum

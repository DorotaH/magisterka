import heapq

MAX_INT = 2 * (10 ** 4) + 1
neighbors = [(-1, 0), (+1, 0), (0, -1), (0, +1)]


class PrioritySet:
	def __init__(self):
		self._byValue = dict()
		self._byPriority = dict()
		self._prioritiesQue = []
		self._prioritiesSet = set()
	
	def add(self, priority, item):
		if item in self._byValue:
			p = self._byValue[item]
			if priority == p:
				return
			self._byPriority[p].remove(item)
		
		if priority not in self._byPriority:
			self._byPriority[priority] = set()
		self._byPriority[priority].add(item)
		self._byValue[item] = priority

		if priority not in self._prioritiesSet:
			self._prioritiesSet.add(priority)
			heapq.heappush(self._prioritiesQue, priority)

	def pop(self):
		priority = self._prioritiesQue[0]
		while len(self._byPriority[priority]) == 0:
			del self._byPriority[priority]
			self._prioritiesSet.remove(priority)
			heapq.heappop(self._prioritiesQue)
			priority = self._prioritiesQue[0]
		
		value = self._byPriority[priority].pop()
		del self._byValue[value]
		return value

	def __len__(self):
		return len(self._byValue)


visits = dict()


def drainWaterFrom(wMap, ogMap, startX, startY):
	toDrain = PrioritySet()
	toDrain.add(0, (startX, startY))
	while len(toDrain) != 0:
		x, y = toDrain.pop()

		# First, we'll look for directions we can drain to
		for _x, _y in neighbors:
			nx, ny = _x + x, y + _y
			if wMap[nx][ny] < wMap[x][y]:
				wMap[x][y] = max(wMap[nx][ny], ogMap[x][y])
		# Then, which ones now drain into this
		for _x, _y in neighbors:
			nx, ny = _x + x, y + _y
			if wMap[nx][ny] > wMap[x][y] and wMap[nx][ny] > ogMap[nx][ny]:
				toDrain.add(wMap[x][y] - wMap[nx][ny], (nx, ny))


class Solution:
	def trapRainWater(self, heightMap: List[List[int]]) -> int:
		waterMap = [len(row) * [MAX_INT] for row in heightMap]
		# We start out by setting the boundaries; we know they can't hold any water
		for i, h in enumerate(heightMap[0]):
			waterMap[0][i] = h
		for i, h in enumerate(heightMap[-1]):
			waterMap[-1][i] = h
		for i in range(len(heightMap)):
			waterMap[i][0] = heightMap[i][0]
			waterMap[i][-1] = heightMap[i][-1]
		# Now, each interior tile's final water height is equal to the minimum of all surrounding tiles (or the original height, if that's higher)
		trapped = 0
		for x, row in enumerate(waterMap):
			for y, h in enumerate(row):
				if h == MAX_INT:
					drainWaterFrom(waterMap, heightMap, x, y)
				trapped += h - heightMap[x][y]
		return trapped


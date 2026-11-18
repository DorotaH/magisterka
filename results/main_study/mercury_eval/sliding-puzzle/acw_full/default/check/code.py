class Solution:
	def slidingPuzzle(self, board: List[List[int]]) -> int:
		
		# dic = {1: (2, 4), 2: (1, 3, 5), 3: (0, 2), 4: (1, 5), 5: (0, 2, 4), 0: (3, 5)} 
		
		dic = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4), 4: (1, 3, 5), 5: (2, 4)}  # cur_pos: next_pos
		
		target = [1, 2, 3, 4, 5, 0]
		queue = deque()
		queue.append((tuple(board[1] + board[0]), 0))
		seen = set()
		seen.add(tuple(board[1] + board[0]))
		
		while queue:
			node, steps = queue.popleft()
			node = list(node)
			if node == target:
				return steps
			
			index = node.index(0)
			for nei in dic[index]:
				node[index], node[nei] = node[nei], node[index]
				if tuple(node) not in seen:
					seen.add(tuple(node))
					queue.append((tuple(node), steps + 1))
				node[index], node[nei] = node[nei], node[index]
		
		return -1
		
		


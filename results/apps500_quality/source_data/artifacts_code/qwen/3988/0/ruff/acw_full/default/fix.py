from collections import defaultdict
from heapq import heappop, heappush


def dijkstra(graph, start):
	n = len(graph)
	dist = [float('inf')] * n
	dist[start] = 0
	pq = [(0, start)]
	while pq:
		current_dist, u = heappop(pq)
		if dist[u] < current_dist:
			continue
		for v, weight in graph[u]:
			distance = current_dist + weight
			if dist[v] > distance:
				dist[v] = distance
				heappush(pq, (distance, v))
	return dist


def solve():
	import sys
	input = sys.stdin.read
	data = input().split()
	
	n = int(data[0])
	m = int(data[1])
	s = int(data[2]) - 1
	
	graph = defaultdict(list)
	undirected_edges = []
	
	index = 3
	for _ in range(m):
		t = int(data[index])
		u = int(data[1 + index]) - 1
		v = int(data[2 + index]) - 1
		index += 3
		
		if t == 1:
			graph[u].append((v, 0))
			graph[v].append((u, 0))
		else:
			graph[u].append((v, 1))
			graph[v].append((u, 1))
			undirected_edges.append((u, v))
	
	# Plan to maximize the number of reachable vertices
	dist_max = dijkstra(graph, s)
	max_reachable = max(dist_max)
	plan_max = ['-' if dist_max[u] < max_reachable else '+' for u in range(n)]
	
	# Plan to minimize the number of reachable vertices
	dist_min = dijkstra(graph, s)
	min_reachable = min(dist_min)
	plan_min = ['+' if min_reachable < dist_min[u] else '-' for u in range(n)]
	
	# Adjust the plans for undirected edges
	for u, v in undirected_edges:
		if dist_max[u] == dist_max[v] and dist_min[u] == dist_min[v]:
			plan_max[u] = '+'
			plan_max[v] = '+'
			plan_min[u] = '-'
			plan_min[v] = '-'
		elif dist_max[u] > dist_max[v]:
			plan_max[u] = '+'
			plan_max[v] = '-'
			plan_min[u] = '-'
			plan_min[v] = '+'
		elif dist_max[u] < dist_max[v] or dist_min[v] < dist_min[u]:
			plan_max[u] = '-'
			plan_max[v] = '+'
			plan_min[u] = '+'
			plan_min[v] = '-'
		else:
			plan_max[u] = '+'
			plan_max[v] = '-'
			plan_min[u] = '-'
			plan_min[v] = '+'
	
	print(max_reachable)
	print(''.join(plan_max))
	print(min_reachable)
	print(''.join(plan_min))


solve()

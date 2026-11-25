import sys
import math
import heapq


def main():
    n = int(input())
    points = []
    for _ in range(n):
        p, c = input().split()
        points.append((int(p), c))

    reds = [point for point in points if point[1] == 'R']
    blues = [point for point in points if point[1] == 'B']
    greens = [point for point in points if point[1] == 'G']

    costs = {}
    for i in range(len(greens)):
        for j in range(i + 1, len(greens)):
            costs[(greens[i], greens[j])] = abs(greens[i][0] - greens[j][0])

    for r in reds:
        for b in blues:
            for g in greens:
                costs[(r, b)] = costs.get((r, b), float('inf'))
                costs[(b, r)] = costs.get((b, r), float('inf'))
                costs[(r, g)] = costs.get((r, g), float('inf'))
                costs[(g, r)] = costs.get((g, r), float('inf'))
                costs[(g, b)] = costs.get((g, b), float('inf'))
                costs[(b, g)] = costs.get((b, g), float('inf'))

    def f(point):
        if point[1] == 'R':
            return 0
        return 1 if point[1] == 'B' else 2

    def g(point):
        if point[1] == 'R':
            return 1
        if point[1] == 'B':
            return 2
        return 0

    def h(point):
        if point[1] == 'R':
            return 1
        if point[1] == 'B':
            return 2
        return 0

    def min_cost():
        pq = []
        visited = set()
        heapq.heappush(pq, (0, (reds[0], greens[0])))
        visited.add((reds[0], greens[0]))
        while pq:
            cost, (r, g) = heapq.heappop(pq)
            if (r, g) == (reds[-1], greens[-1]):
                return cost
            for p in points:
                if p not in visited:
                    new_cost = costs[(r, p)] + cost + costs[(p, g)]
                    if f(p) != f(r) and f(p) != f(g) and (p not in visited):
                        heapq.heappush(pq, (new_cost, (r, p)))
                        visited.add(p)
                    elif g(p) != g(r) and g(p) != g(g) and (p not in visited):
                        heapq.heappush(pq, (new_cost, (p, g)))
                        visited.add(p)
                    elif h(p) != h(r) and h(p) != h(g) and (p not in visited):
                        heapq.heappush(pq, (new_cost, (r, p)))
                        visited.add(p)
        return -1

    print(min_cost())


if __name__ == "__main__":
    main()

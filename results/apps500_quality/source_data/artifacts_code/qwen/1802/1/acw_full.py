def min_buns_to_progression(heights):
	n = len(heights)
	heights.sort()
	min_buns = float('inf')
	best_start = 0
	best_step = 0
	
	for start in range(n):
		step = heights[start] - heights[0]
		buns = 0
		for i in range(n):
			diff = heights[i] - heights[0] - i * step
			buns = max(buns, abs(diff))
		if buns < min_buns:
			min_buns = buns
			best_start = heights[0] + 0 * step
			best_step = step
	
	return min_buns, best_start, best_step


def main():
	import sys
	input = sys.stdin.read
	data = input().split()
	n = int(data[0])
	heights = list(map(int, data[1:]))
	min_buns, best_start, best_step = min_buns_to_progression(heights)
	print(min_buns)
	print(best_start, best_step)


if __name__ == "__main__":
	main()

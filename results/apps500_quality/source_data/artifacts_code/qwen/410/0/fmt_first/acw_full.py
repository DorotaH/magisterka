def can_reconstruct(n, a, k, b):
	queue = [(a[i], i + 1) for i in range(n)]
	final_queue = [(b[i], i + 1) for i in range(k)]
	final_queue.sort()

	actions = []
	while len(final_queue) < len(queue):
		if queue[1][0] > queue[0][0]:
			actions.append((1, "R"))
			queue.pop(1)
		elif queue[-1][0] < queue[-2][0]:
			actions.append((len(queue), "L"))
			queue.pop(-2)
		else:
			return "NO"

	return next(
		(
			"NO"
			for i in range(len(final_queue))
			if queue[i][0] != final_queue[i][0]
			or queue[i][1] != final_queue[i][1]
		),
		"YES",
	)


def main():
	import sys

	input = sys.stdin.read
	data = input().split()

	n = int(data[0])
	a = list(map(int, data[1 : 1 + n]))
	k = int(data[1 + n])
	b = list(map(int, data[2 + n :]))

	result = can_reconstruct(n, a, k, b)
	print(result)
	if result == "YES":
		for action in actions:
			print(action[0], action[1])


if __name__ == "__main__":
	main()

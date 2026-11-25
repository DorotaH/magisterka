import sys
input = sys.stdin.readline


def get_values():
	n, k = map(int, input().split())
	notes = list(map(int, input().split()))
	return n, k, notes


def solve(n, k, notes):
	max_val = 0
	for note in notes:
		max_val = max(max_val, note % k)

	answer = set()
	i = 1
	while i * k <= max_val:
		i += 1

	for note in notes:
		rem = note % k
		if rem in answer:
			answer.add(0)
		else:
			answer.add(i * k - rem)

	answer = sorted(list(answer))
	return len(answer), answer


n, k, notes = get_values()
answer_length, answer = solve(n, k, notes)
print(answer_length)
print(*answer)

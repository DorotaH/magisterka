from collections import Counter
from sys import stdin


def main():
	n, m = map(int, stdin.readline().split())
	student_answers = [stdin.readline().strip() for _ in range(n)]
	scores = list(map(int, stdin.readline().split()))

	max_score = 0
	for i in range(m):
		choices = [student_answers[j][i] for j in range(n)]
		freq = Counter(choices)
		max_freq = max(freq.values())
		max_score += scores[i] * max_freq

	print(max_score)


if __name__ == "__main__":
	main()

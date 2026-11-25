from sys import stdin


def main():
	n = int(stdin.readline())
	prizes = list(map(int, stdin.readline().split()))

	def find_min_time():
		if n == 1:
			return abs(prizes[0] - 1) + abs(1000000 - prizes[0])

		left, right = 1, prizes[0]
		last_prize = 0
		time = 0
		for i in range(1, n):
			if prizes[i] - prizes[i - 1] <= right - left:
				time += max(abs(prizes[i] - left), abs(right - prizes[i]))
				left = prizes[i]
			else:
				time += abs(prizes[i] - right) + max(abs(prizes[i - 1] - left), abs(right - prizes[i - 1])
						)
				right = prizes[i]
			last_prize = prizes[i]

		return max(abs(prizes[n - 1] - left), abs(right - prizes[n - 1])) + time

	print(find_min_time())


if __name__ == "__main__":
	main()

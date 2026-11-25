import sys


def main():
	input = sys.stdin.read
	data = input().split()

	N = int(data[0])
	M = int(data[1])
	likes = [set(map(int, data[2 + i * 2:2 + i * 2 + K])) for i, K in enumerate(range(1, N + 1), start=1)]

	common_likes = likes[0]
	for i in range(1, N):
		common_likes &= likes[i]

	print(len(common_likes))


if __name__ == "__main__":
	main()
